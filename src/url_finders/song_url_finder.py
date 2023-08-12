"""

"""


# import requests
import logging
import time

# import bs4
# from bs4 import BeautifulSoup
from googlesearch import search
from youtubesearchpython import VideosSearch

# import selenium
from src.helpers import now

# import logging

# import threading

# import time
# from googlesearch import search

from src.url_finders.helpers import ThreadManager

# from src.helpers import now


def _build_query(
    song,
    website,
    author: str = "",
    tab: str = "",
    live: str = "",
):
    # song
    query = str(song)

    # author
    if author:
        query += f" {author}"

    # if tab
    if tab:
        query += " tab"

    # if live
    if live:
        query += " live"

    # website
    if website and website != "youtube":
        query += f" {website}"

    query = query.replace("  ", " ").replace("  ", " ").lower().strip()

    return query


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
        timeout=15,
        live="",
        engine="youtubesearchpython",
        verbose: int = 1,  # useless
    ) -> list[str]:
        """ """

        # build query
        query = _build_query(
            song=song,
            website=website,
            author=author,
            live=live,
        )
        logging.info(f"query : {query}")

        # from youtubesearchpython import VideosSearch

        t1 = -1
        t0 = time.time()

        dd = {
            "_query": query,
            "_date": now(),
            "_timeout": timeout,
            "_song": song,
            "_author": author,
            "_engine": engine,
            "_website": website,
            "_live": live,
            "_limit": limit,
            "_robust": -1,
        }

        # search
        try:
            search = VideosSearch(query, limit=limit)
            response = search.result()
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

        # results
        try:
            results = response["result"]
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

        if not results:
            response = {
                "url_list": [],
                "status": 502,
                "comment": "no url found",
                "candidates": [],
                "time": t1,
            }
            response.update(dd)
            return response

        url = results[0]["link"]

        response = {
            "url_list": [url],
            "status": 200,
            "comment": "OK",
            "candidates": [results[i]["link"] for i in range(limit)],
            "time": t1,
        }
        response.update(dd)
        return response

    @classmethod
    def robust_video(
        self,
        song: str,
        author: str = "",
        website: str = "youtube",
        limit: int = 5,
        timeout=15,
        live="",
        engine="youtubesearchpython",
        verbose: int = 1,  # useless
    ) -> list[str]:
        """ " """

        f = SongUrlFinder.video

        tm = ThreadManager(
            f,
            timeout=timeout,
            song=song,
            author=author,
            website=website,
            engine=engine,
            limit=limit,
            live=live,
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
                "_live": live,
                "_engine": engine,
                "_website": website,
                "_limit": limit,
                "_robust": 1,
            }

    @classmethod
    def tab(
        self,
        song: str,
        website: str,
        author: str = "",
        tab: bool = True,
        timeout: int = 15,
        engine="googlesearch-python",
        limit: int = 5,
        live="",
        verbose: int = 1,  # useless
    ) -> dict:
        """ """

        # website_list
        website_list = [
            "ultimate",
            "ultimate-guitar",
            "ultimateguitar",
            "boiteachansons",
            "boite",
            "bac",
        ]
        if not website.lower() in website_list:
            raise AttributeError(
                f"website {website} not in website_list {website_list}"
            )

        # tab
        tab = int(tab)
        tab = "tab" if tab else ""

        # manage website
        if "ultimate" in website.lower():
            website = "ultimate-guitar"

        if (website.lower() == "bac") or ("boite" in website.lower()):
            website = "boiteachansons"

        # lang and domain
        lang = "fr" if "boite" in website else "en"
        domain = "fr" if "boite" in website else "com"

        # build query
        query = _build_query(
            song=song,
            website=website,
            author=author,
            tab=tab,
            live=live,
        )
        logging.info(f"query : {query}")

        # do search
        if not engine == "googlesearch-python":
            raise NotImplementedError("Only googlesearch-python is implemented")

        t1 = -1
        t0 = time.time()

        dd = {
            "_query": query,
            "_date": now(),
            "_timeout": timeout,
            "_song": song,
            "_author": author,
            "_tab": tab,
            "_live": live,
            "_engine": engine,
            "_website": website,
            "_limit": limit,
            "_robust": -1,
        }

        # search
        try:
            li = search(query, lang=lang, num_results=limit, timeout=timeout)
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
        _url_list = [i for i in url_list if website in i]
        if not _url_list:
            response = {
                "url_list": [],
                "status": 503,
                "comment": f"no website {website} in query {query}",
                "candidates": url_list,
                "time": t1,
            }
            response.update(dd)
            return response

        # filter good route
        pattern = "partition" if website == "boiteachansons" else "tab"
        if pattern:
            __url_list = [i for i in _url_list if pattern in i]
            if not __url_list:
                response = {
                    "url_list": [],
                    "status": 504,
                    "comment": f"no pattern {pattern}  for {website} in query {query}",
                    "candidates": url_list,
                    "time": t1,
                }
                response.update(dd)
                return response
        else:
            __url_list = _url_list

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
        website: str,
        author: str = "",
        tab: bool = True,
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
                "_robust": 1,
            }

    @classmethod
    def wiki(self):
        pass
