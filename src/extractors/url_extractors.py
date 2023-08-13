"""
"""

import os, logging

from src.cleaners import Cleaner


class UrlExtractor:
    """ """

    @classmethod
    def author(
        self,
        url: str,
        website: str,
    ) -> str:
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

        if not (("boite" in website) or ("ultimate" in website)):
            raise NotImplementedError(f"website not implemented : {website}")

        try:
            url = url.split("/")
            url = url[-2]
            url = Cleaner.url.author_song(url)
            return url

        except Exception as e:
            logging.error(f"{e} ==> {url}")

            return ""

    @classmethod
    def song(
        self,
        url: str,
        website: str,
    ) -> str:
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

        if not (("boite" in website) or ("ultimate" in website)):
            raise NotImplementedError(f"website not implemented : {website}")

        try:
            url = url.split("/")
            url = url[-1]
            url = Cleaner.url.author_song(url)
            return url

        except Exception as e:
            logging.error(f"{e} ==> {url}")

            return ""
