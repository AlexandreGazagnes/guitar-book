"""
UrlManager : scrap url from song /author + tab + webiste google search
"""

import os, sys, time, logging

import pandas as pd


from src.loaders import Loader
from src.url_finders import UrlFinder
from src.scrappers import Scrapper
from src.helpers import now

from src.managers.helpers import HelperManager
from src.extractors import Extractor

# import requests
# from src.cleaners import clean_author_from_url

from src.validators import Validator

from src.cleaners import Cleaner


class UrlManager:
    """UrlManager : scrap url from song /author + tab + webiste google search

    public methods:
        - run : preform all

    private methods :
        - _load_base
        - _sample
        - _extract_author
        - _prepare_list_dict
        - _update_and_save
    """

    @classmethod
    def _load_base(
        self,
        website: str,
        nan_url="keep",
        not_processed="only",
        top=0,
    ):
        """load data base using params and create __query column"""

        logging.debug("UrlManager._load_base")

        website = Cleaner.txt.webiste(
            website, with_validation=True, authorise_none=True
        )

        df = Loader.base(
            website=website,
            nan_url=nan_url,
            top=top,
            not_processed=not_processed,
        )

        # author
        df.author.fillna("", inplace=True)

        # __query
        df["__query"] = df.song + " " + df.author
        df["__query"] = df["__query"].str.strip()
        df["__query"] = df["__query"].apply(
            lambda i: i.replace("  ", " ").replace("  ", " ")
        )

        return df

    @classmethod
    def _scrap_urls(
        self,
        df: pd.DataFrame,
        website: str,
        asynch: bool = False,
    ):
        """scrap url with finder_url_manager"""

        website = Cleaner.txt.website(
            website, with_validation=True, authorise_none=False
        )

        logging.debug("UrlManager._scrap_urls")

        _df = df.copy()

        if not asynch:
            _df["__url"] = _df["__query"].apply(
                lambda query: HelperManager._finder_url_manager(
                    query,
                    website=website,
                )
            )
        else:
            _df["__url"] = _df["__query"].parallel_apply(
                lambda query: HelperManager._finder_url_manager(query, website=we)
            )

        return _df

    @classmethod
    def _prepare_list_dict(self, df):
        """transform list of dict k, v with id and __url"""

        logging.debug("UrlManager._prepare_list_dict")
        # cols = ["id", "__url"]
        # _df = df.loc[:, cols]
        # li = _df.to_dict(orient="records")
        # li

        li = HelperManager._prepare(df, key="__url")

        return li

    @classmethod
    def _update_and_save(
        self,
        li: list,
        website: str,
        filename: str,
        path="./data/",
    ):
        """reload a entier base and update id / _url if neeeded, save final"""

        website = Cleaner.txt.website(
            website, with_validation=True, authorise_none=False
        )

        logging.debug("UrlManager._update_and_save")

        fn = os.path.join(path, filename)

        _df = HelperManager._update_save(li, dest_key="url", fn=fn, website=website)

        return _df

    # @classmethod
    # def run(
    #     self,
    #     top: int = 10,
    #     n_sample: int = -1,
    #     verbose: int = 1,
    # ):
    #     """load, sample, scrap, prepare and update/save final"""

    #     logging.info("UrlManager.run")

    #     df = self._load_base(
    #         website="",
    #         nan_url="keep",
    #         top=top,
    #     )

    #     if not len(df):
    #         logging.warning(f"df empty : {len(df)} ")
    #         return 0

    #     df = HelperManager._sample(df, n_sample=n_sample)
    #     df = self._scrap_urls(df)
    #     li = self._prepare_list_dict(df)
    #     self._update_and_save(li)

    #     return 1
