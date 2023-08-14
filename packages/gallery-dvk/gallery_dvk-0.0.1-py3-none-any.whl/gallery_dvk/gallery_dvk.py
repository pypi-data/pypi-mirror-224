#!/usr/bin/env python3

import os
import argparse
import python_print_tools.printer
from gallery_dvk.extractor.transfur import Transfur
from os.path import abspath, exists

class GalleryDVK():
    def __init__(self):
        """
        Creates the GalleryDVK class.
        """
        self.extractors = []
    
    def __enter__(self):
        """
        Setup for when GallerDVK is opened.
        Create an object for each Extractor.
        """
        self.extractors = [Transfur()]
        return self
        
    def __exit__(self, *args):
        """
        Cleanup for GalleryDVK once it is closed.
        """
        for extractor in self.extractors:
            extractor.__exit__()

    def download_from_url(self, url:str, directory:str) -> bool:
        """
        Attepts to download media from a given URL.
        Returns False if the URL is for an unsupported site.
        
        :param url: URL to attempt downloading
        :type url: str, required
        :param directory: Directory to save into
        :type directory: str, required
        :return: Whether the download completed successfully
        :rtype: bool
        """
        for extractor in self.extractors:
            if extractor.download_from_url(url, directory):
                return True
        python_print_tools.printer.color_print(f"Unsupported URL: {url}", "r")
        return False

def main():
    """
    Sets up downloading from Transfur.com
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "URL",
        help="URL to download.",
        type=str)
    parser.add_argument(
        "-d",
        "--directory",
        help="Directory in which to save media.",
        nargs="?",
        type=str,
        default=str(os.getcwd()))
    args = parser.parse_args()
    full_directory = abspath(args.directory)
    if not exists(full_directory):
        python_print_tools.printer.color_print("Invalid directory", "r")
    else:
        with GalleryDVK() as dvk:
            dvk.download_from_url(args.URL, full_directory)