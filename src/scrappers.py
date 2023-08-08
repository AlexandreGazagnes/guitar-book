"""
All class and function need to acces internet to search, download scrap
"""

import requests
import logging

import bs4
from bs4 import BeautifulSoup
from googlesearch import search

import selenium


class TabScrapper:
    """ """

    @classmethod
    def scrap(
        self,
        url: str,
        verbose: int = 1,  # useless
    ) -> str:
        """ """

        # url not str
        if (not url) or (not isinstance(url, str)):
            logging.error(f"url empty or not string : {url}, type {type(url)}")
            return ""

        # url not good website
        if not url.startswith("https://www.boiteachansons"):
            logging.error(f"Not a valid website : {url}")
            return ""

        # url not good route
        if not "partition" in url:
            logging.error(f"maybe not a valid url : {url}")
            return ""

        # requests
        try:
            html_doc = requests.get(url).content
            return html_doc
        except Exception as e:
            logging.error(f"{e} => {url}")
            return ""

    @classmethod
    def scrap_save(
        self,
        url: str,
        dest: str = "./data/raw/boiteachansons/",
        verbose: int = 1,  # useless
    ) -> int:  # status code as return
        """ """

        logging.info(url)

        # scrap
        html_doc = self.scrap(url=url, verbose=verbose)

        # if none
        if not html_doc or len(str(html_doc)) < 100:
            logging.error(f"invalid html : {html_doc} for {url}")
            return 1

        # song and auth
        song = url.split("/")[-1]
        auth = url.split("/")[-2]

        # soup
        soup = BeautifulSoup(html_doc, "html.parser")

        # retired song
        msg = "Le titulaire des droits de reproduction graphique"
        if msg in soup.text:
            logging.error(f"Chanson retirée : {auth} {song} => {url}")
            fn = f"{dest}RETIRED_{auth}___{song}.html"
            open(fn, "w").close()
            return 0

        # fn
        fn = f"{dest}{auth}___{song}.html"
        logging.info(f"Saving to {fn}")

        # save
        with open(fn, "w") as f:
            f.write(soup.prettify())

        return 0


class VideoScrapper:
    """ """

    @classmethod
    def scrap_save(self, url: str) -> int:
        """ """
        logging.critical("NOT IMPLEMENTED")

        return 1


class UrlSongFinder:
    """Methids to find ulr list from a specific queryg

    Public Methods :
        - video : youtube list of url video for a song
        - tab : boiteachnason or other list of url tab for a song

    """

    @classmethod
    def video(
        self,
        song: str,
        author: str = "",
        website: str = "youtube",
        limit: int = 5,
        verbose: int = 1,  # useless
    ) -> list[str]:
        """ """

        logging.critical("NOT IMPLEMENTED")

        return []

    @classmethod
    def tab(
        self,
        song: str,
        author: str = "",
        website: str = "boiteachansons",
        # engine="duckduckgo",
        limit: int = 5,
        verbose: int = 1,  # useless
    ) -> list[str]:
        """ """

        # lang
        lang = "fr" if "boite" in website else "com"

        # build query
        q = str(song)
        if author:
            q += f" {author}"
        q += " tab"
        if website:
            q += f" {website}"

        logging.info(q)

        # do search
        li = search(q, lang=lang, num_results=limit)

        # urls
        url_list = [url for url in li]

        # filter good website
        url_list = [i for i in url_list if "boite" in i]

        # filter good route
        url_list = [i for i in url_list if "partition" in i]
        if not url_list:
            logging.warning(f"No tab found for {q}")

        return url_list[:limit]

    @classmethod
    def wiki(self):
        pass


class Scrapper:
    video = VideoScrapper
    tab = TabScrapper


class UrlFinder:
    song = UrlSongFinder
