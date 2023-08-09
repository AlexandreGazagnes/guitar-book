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
        tab: str = "tab",
        website: str = "boiteachansons",
        timeout: int = 15,
        engine="googlesearch-python",
        limit: int = 5,
        verbose: int = 1,  # useless
    ) -> dict:
        """ """

        # lang fr if boiteachansons else com
        lang = "fr" if "boite" in website else "com"

        # build query

        # song
        q = str(song)

        # author
        if author:
            q += f" {author}"

        # if tab
        if tab:
            q += " tab"

        # website
        if website:
            q += f" {website}"

        logging.info(q)

        # do search
        if not engine == "googlesearch-python":
            raise NotImplementedError("Only googlesearch-python is implemented")

        t1 = -1
        t0 = time.time()

        dd = {
            "_query": q,
            "_date": now(),
            "_timeout": timeout,
            "_song": song,
            "_author": author,
            "_tab": tab,
            "_engine": engine,
            "_website": website,
            "_limit": limit,
            "_robust": 1,
        }

        # search
        try:
            li = search(q, lang=lang, num_results=limit, timeout=timeout)
            t1 = round(time.time() - t0, 4)
        except Exception as e:
            t1 = round(time.time() - t0, 4)

            results = {
                "url_list": [],
                "status": 500,
                "comment": f"error : {e}",
                "candidates": [],
                "time": t1,
            }
            results.update(dd)
            return results

        # urls
        try:
            url_list = [url for url in li]
            t1 = round(time.time() - t0, 4)

        except Exception as e:
            t1 = round(time.time() - t0, 4)

            results = {
                "url_list": [],
                "status": 501,
                "comment": f"error : {e}",
                "candidates": [],
                "time": t1,
            }
            results.update(dd)
            return results

        if not url_list:
            results = {
                "url_list": [],
                "status": 502,
                "comment": "no url found",
                "candidates": [],
                "time": t1,
            }
            results.update(dd)
            return results

        # filter good website
        _url_list = [i for i in url_list if "boite" in i]
        if not _url_list:
            results = {
                "url_list": [],
                "status": 503,
                "comment": "no boite in url",
                "candidates": url_list,
                "time": t1,
            }
            results.update(dd)
            return results

        # filter good route
        __url_list = [i for i in _url_list if "partition" in i]
        if not __url_list:
            results = {
                "url_list": [],
                "status": 504,
                "comment": "no partition in url",
                "candidates": url_list,
                "time": t1,
            }
            results.update(dd)
            return results

        results = {
            "url_list": __url_list[:limit],
            "status": 200,
            "comment": "OK",
            "candidates": url_list,
            "time": t1,
        }
        results.update(dd)
        return results

    @classmethod
    def robust_tab(
        self,
        song: str,
        author: str = "",
        tab: str = "tab",
        website: str = "boiteachansons",
        timeout: int = 15,
        engine="googlesearch-python",
        limit: int = 5,
        verbose: int = 1,  # useless
    ) -> dict:
        """ """

        f = UrlSongFinder.tab

        tm = ThreadManager(
            f,
            timeout=timeout,
            song=song,
            author=author,
            tab=tab,
            website=website,
            engine=engine,
            limit=limit,
        )
        t0 = time.time()

        try:
            return tm.run()
        except Exception as e:
            t1 = time.time() - t0
            logging.error(e)
            return {
                "url_list": [],
                "status": 555,
                "comment": f"{e}",
                "candidates": [],
                "time": t1,
                #
                "_query": "--no query for robust tab",
                "_date": now(),
                "_timeout": timeout,
                "_song": song,
                "_author": author,
                "_tab": tab,
                "_engine": engine,
                "_website": website,
                "_limit": limit,
                "_robust": 0,
            }

    @classmethod
    def wiki(self):
        pass


class Scrapper:
    video = VideoScrapper
    tab = TabScrapper


class UrlFinder:
    song = UrlSongFinder
