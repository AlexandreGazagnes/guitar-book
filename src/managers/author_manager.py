"""
Author Manager : extract author based on url
"""

import pandas as pd
import requests
from src.loaders import Loader
from src.url_finders import UrlFinder
from src.helpers import now
import os, sys, time, logging

# from src.cleaners import clean_author_from_url
from src.extractors import Extractor


class AuthorManager:
    """Author Manager : extract author based on url

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
        website: str = "boiteachansons",
        author_notna: str = "drop",
        nan_url: str = "drop",
        not_processed: str = "drop",
        top=0,
    ) -> pd.DataFrame:
        """load data base using params and create __query column"""

        logging.debug("AuthorManager._load_base")

        df = Loader.base(website=website, nan_url=nan_url, top=top)

        assert author_notna in [None, False, 0, "drop", "keep", "ignore"]

        # # if author_notna == "drop " :
        # if author_notna == "drop":
        #     df = df.loc[df.author.isna()]

        return df

    @classmethod
    def _extract_author(self, df: pd.DataFrame) -> pd.DataFrame:
        """_extract_author from url to a colonum"""

        logging.debug("AuthorManager._extrct_author")

        _df = df.copy()
        _df["__author"] = ""

        _df["__author"] = _df["url"].apply(extract_author_from_url)

        return _df

    @classmethod
    def _extract_song(self, df: pd.DataFrame) -> pd.DataFrame:
        """_extract_song from url to a colonum"""

        logging.debug("AuthorManager._extrct_song")

        _df = df.copy()
        _df["__song"] = ""

        _df["__song"] = _df["url"].apply(extract_song_from_url)

        return _df

    @classmethod
    def _prepare_list_dict(
        self, df: pd.DataFrame, source_key: str = "__author"
    ) -> list[dict]:
        """transform list of dict k, v with id and __url"""

        logging.debug("AuthorManager._prepare_list_dict")

        return HelperManager._prepare(df, source_key)

    @classmethod
    def _update_and_save(
        self,
        li: list,
        dest_key: str = "_author",
        fn: str = "./data/base.csv",
    ) -> pd.DataFrame:
        """update base df and save updated df"""

        logging.debug("AuthorManager._update_and_save")

        _df = HelperManager._update_save(li, dest_key=dest_key, fn=fn)

        return _df

    @classmethod
    def run(
        self,
        top: int = 10,
        n_sample: int = -1,
        verbose: int = 1,
    ) -> pd.DataFrame:
        """run all autononous :

        df = self._load_base()
        df = self._sample(df, n=-1)
        df = self._extract_author(df)
        li = self._prepare_list_dict(df)
        self._update_and_save(li)

        """

        logging.debug("AuthorManager.run")

        df = self._load_base(
            website="boiteachansons",
            author_notna="drop",
            nan_url="drop",
            top=top,
        )

        if not len(df):
            logging.warning(f"df empty : {len(df)} ")
            return 0

        df = HelperManager.HelperManager.__sample(df, n_sample)
        df = self._extract_author(df)
        li = self._prepare_list_dict(df)
        df = self._update_and_save(li)

        return df
