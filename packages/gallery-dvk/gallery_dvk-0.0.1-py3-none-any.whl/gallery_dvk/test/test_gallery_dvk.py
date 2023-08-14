#!/usr/bin/env python3

import os
import metadata_magic.file_tools as mm_file_tools
from gallery_dvk.gallery_dvk import GalleryDVK
from gallery_dvk.extractor.transfur import Transfur
from os.path import abspath, join

def test_download_from_url():
    """
    Tests the download_from_url method.
    """
    with GalleryDVK() as dvk:
        # Test downloading from a supported URL
        dvk.extractors.insert(0, Transfur([]))
        temp_dir = mm_file_tools.get_temp_dir()
        assert dvk.download_from_url("http://transfur.com/Users/Dondedun/Submissions/23415", temp_dir)
        sub_dir = abspath(join(temp_dir, "Transfur"))
        sub_dir = abspath(join(sub_dir, "Dondedun"))
        assert os.listdir(sub_dir) == ["Be A-Were - Werecat TF.png"]
        assert os.stat(abspath(join(sub_dir, "Be A-Were - Werecat TF.png"))).st_size == 479281
        # Test downloading from an unsupported URL
        assert not dvk.download_from_url("Not Applicable", temp_dir)
        assert not dvk.download_from_url("google.com/whatever", temp_dir)