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


class ArtistBioScrapper:
    """Artist Bio Scrapper Class
    ---- NOT IMPLEMENTED ----

    methods :
        - scrap_save : scrap and save artist bio

    return :
        - dict with url, status, comment, date, html_doc"""

    @classmethod
    def scrap_save(self, url: str) -> int:
        """ """
        logging.critical("NOT IMPLEMENTED")

        return 1
