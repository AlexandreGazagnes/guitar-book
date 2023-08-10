"""

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

from src.url_finders.helpers import ThreadManager
from src.helpers import now


class SongUrlFinder:
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

            response = {
                "url_list": [],
                "status": 500,
                "comment": f"error : {e}",
                "candidates": [],
                "time": t1,
            }
            response.update(dd)
            return response

        # urls
        try:
            url_list = [url for url in li]
            t1 = round(time.time() - t0, 4)

        except Exception as e:
            t1 = round(time.time() - t0, 4)

            response = {
                "url_list": [],
                "status": 501,
                "comment": f"error : {e}",
                "candidates": [],
                "time": t1,
            }
            response.update(dd)
            return response

        if not url_list:
            response = {
                "url_list": [],
                "status": 502,
                "comment": "no url found",
                "candidates": [],
                "time": t1,
            }
            response.update(dd)
            return response

        # filter good website
        _url_list = [i for i in url_list if "boite" in i]
        if not _url_list:
            response = {
                "url_list": [],
                "status": 503,
                "comment": "no boite in url",
                "candidates": url_list,
                "time": t1,
            }
            response.update(dd)
            return response

        # filter good route
        __url_list = [i for i in _url_list if "partition" in i]
        if not __url_list:
            response = {
                "url_list": [],
                "status": 504,
                "comment": "no partition in url",
                "candidates": url_list,
                "time": t1,
            }
            response.update(dd)
            return response

        response = {
            "url_list": __url_list[:limit],
            "status": 200,
            "comment": "OK",
            "candidates": url_list,
            "time": t1,
        }
        response.update(dd)
        return response

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

        f = SongUrlFinder.tab

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
