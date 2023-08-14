#!/usr/bin/env python3

import os
import metadata_magic.file_tools as mm_file_tools
from gallery_dvk.gallery_dvk import GalleryDVK
from gallery_dvk.test.extractor.dummy_extractor import DummyExtractor
from os.path import abspath, join

def test_download_from_url():
    """
    Tests the download_from_url method.
    """
    with GalleryDVK() as dvk:
        # Test downloading from a supported URL
        dvk.extractors.insert(0, DummyExtractor([]))
        temp_dir = mm_file_tools.get_temp_dir()
        assert dvk.download_from_url("https://www.pythonscraping.com/img/gifts/img3.jpg", temp_dir)
        assert os.listdir(temp_dir) == ["Test Title!.jpg"]
        assert os.stat(abspath(join(temp_dir, "Test Title!.jpg"))).st_size == 71638
        # Test downloading from an unsupported URL
        assert not dvk.download_from_url("Not Applicable", temp_dir)
        assert not dvk.download_from_url("google.com/whatever", temp_dir)