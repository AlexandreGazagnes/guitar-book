"""
All class and function need to acces internet to search, download scrap
"""

import requests
import logging
import time

import bs4
from bs4 import BeautifulSoup
from googlesearch import search

import selenium
from src.helpers import now

# import logging

import threading

# import time
# from googlesearch import search

from src.threaders import ThreadManager
from src.helpers import now


class SongVideoScrapper:
    """SongVideoScrapper
    ---- NOT IMPLEMENTED ----

    methods :
        - scrap : scrap song video"""

    @classmethod
    def scrap_save(self, url: str) -> int:
        """ """
        logging.critical("NOT IMPLEMENTED")

        return 1
