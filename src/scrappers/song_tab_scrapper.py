"""

"""

import requests
import logging

from bs4 import BeautifulSoup
from googlesearch import search

from src.helpers import now
from src.validators import Validator

# import time
# import bs4
# import selenium
# import logging
# import threading
# import time
# from googlesearch import search
# from src.threaders import ThreadManager


class SongTabScrapper:
    """Song Tab Scrapper Class

    methods :
        - scrap : scrap song tab
        - scrap_save : scrap and save song tab

    return :
        - dict with url, status, comment, date, retired, html_doc
    """

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
            return {
                "url": url,
                "status": 500,
                "comment": f"url empty or not string : {url}, type {type(url)}",
                "date": now(),
                "retired": -1,
                "html_doc": "",
            }

        # valid website
        try:
            Validator.tab_url(url, authorise_none=False)
        except Exception as e:
            logging.error(f"Not a valid website : {url}")
            logging.error(e)
            return {
                "url": url,
                "status": 501,
                "comment": f"url empty or not string : {url}, type {type(url)} ==> error is : {e}",
                "date": now(),
                "retired": -1,
                "html_doc": "",
            }

        # valid pattern in url tab website
        try:
            Validator.tab_url_pattern(url)
        except Exception as e:
            logging.error(f"maybe not a valid pattern url : {url}")
            logging.error(e)
            return {
                "url": url,
                "status": 502,
                "comment": f"maybe not a valid url : {url} -- no good patter. error : {e}",
                "date": now(),
                "retired": -1,
                "html_doc": "",
            }

        # requests
        try:
            html_doc = requests.get(url).content
            return {
                "url": url,
                "status": 200,
                "comment": "OK",
                "date": now(),
                "retired": -1,
                "html_doc": html_doc,
            }
        except Exception as e:
            logging.error(f"{e} => {url}")
            return {
                "url": url,
                "status": 504,
                "comment": f"requests failed : error {e} => {url}",
                "date": now(),
                "retired": -1,
                "html_doc": "",
            }

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
        response = self.scrap(url=url, verbose=verbose)
        if int(response["status"]) != 200:
            logging.error(response)
            return response

        # if none
        if not response["html_doc"] or len(str(response["html_doc"])) < 100:
            response["status"] = 505
            response["comment"] = "html_doc empty or too short"
            logging.error(response)
            return response

        # song and auth
        song = url.split("/")[-1]
        auth = url.split("/")[-2]

        # soup
        soup = BeautifulSoup(response["html_doc"], "html.parser")

        # retired song
        msg = "Le titulaire des droits de reproduction graphique"
        if msg in soup.text:
            response["status"] = 506
            response["retired"] = 1
            response["comment"] = f"Chanson retirée : {auth} {song} => {url}"
            response["html_doc"] = "Le titulaire des droits de reproduction graphique"
            logging.error(response)

            fn = f"{dest}RETIRED_{auth}___{song}.html"
            open(fn, "w").close()
            return response

        # fn
        fn = f"{dest}{auth}___{song}.html"
        logging.info(f"Saving to {fn}")

        # save
        with open(fn, "w") as f:
            f.write(soup.prettify())

        response["status"] = 201
        response["retired"] = 0
        response["comment"] = f"OK scraped and saved : {auth} {song} => {url}"

        return response
