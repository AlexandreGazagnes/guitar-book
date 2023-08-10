"""
"""

import os, logging

from src.cleaners import clean_author_song_from_url


class UrlExtractor:
    """ """

    @classmethod
    def author(self, url: str) -> str:
        """helper function t oextract author from an url

        SHOULD BE IN AN EXTRACTOR MODULE
        """

        logging.info(url)

        if not isinstance(url, str):
            logging.error(f"url {url} not a str : {type(url)}")
            return ""

        if not url:
            logging.error(f"{url} is null")
            return ""

        if not "/" in url:
            logging.error(f"/ not in url : {url}")
            return ""

        try:
            url = url.split("/")
            url = url[-2]
            url = clean_author_song_from_url(url)
            return url

        except Exception as e:
            logging.error(f"{e} ==> {url}")

            return ""

    @classmethod
    def song(self, url: str) -> str:
        """helper function t oextract song from an url

        SHOULD BE IN AN EXTRACTOR MODULE
        """

        logging.info(url)

        if not isinstance(url, str):
            logging.error(f"url {url} not a str : {type(url)}")
            return ""

        if not url:
            logging.error(f"{url} is null")
            return ""

        if not "/" in url:
            logging.error(f"/ not in url : {url}")
            return ""

        try:
            url = url.split("/")
            url = url[-1]
            url = clean_author_song_from_url(url)
            return url

        except Exception as e:
            logging.error(f"{e} ==> {url}")

            return ""
