"""
Managers modules
"""

import pandas as pd
import requests
from src.loaders import Loader
from src.scrappers import UrlFinder
from src.helpers import now
import os, sys, time, logging

# from src.cleaners import clean_author_from_url
from src.extractors import extract_author_from_url


class HelperManager:
    """ """

    @classmethod
    def _sample(self, df, n_sample=10):
        """sample random n"""

        logging.debug("__sample")
        if (n_sample == -1) or (not n_sample):
            return df

        df = df.copy()
        df = df.sample(n_sample)

        return df

    @classmethod
    def _finder_url_manager(self, i: str) -> str:
        """helper function to decore a  UrlFinder.song_tab(i) call"""

        try:
            ans = UrlFinder.song.tab(i)
            if len(ans):
                return ans[0]

            logging.error()
            logging.error(f"emplty list {ans} => {i} ")
            return ""

        except Exception as e:
            logging.error(f"{e} => {i} ")
            return ""

    @classmethod
    def _prepare(self, df, key):
        """ """

        cols = ["id", key]
        _df = df.loc[:, cols]
        _df.columns = ["id", "key"]
        li = _df.to_dict(orient="records")
        li

        return li

    @classmethod
    def _update_save(self, li, dest_key, fn):
        """ """

        df = Loader.base(website="", nan_url="", top=None)

        for dd in li:
            try:
                k, v = dd["id"], dd["key"]
                df.loc[df["id"] == int(k), dest_key] = v

            except Exception as e:
                print(e)

        df.to_csv(fn, index=False)

        return df


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
        top=10,
    ) -> pd.DataFrame:
        """load data base using params and create __query column"""

        logging.debug("AuthorManager._load_base")

        df = Loader.base(website=website, nan_url=nan_url, top=top)

        if author_notna == "drop":
            df = df.loc[df.author.isna()]

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
    def _prepare_list_dict(self, df: pd.DataFrame) -> list[dict]:
        """transform list of dict k, v with id and __url"""

        logging.debug("AuthorManager._prepare_list_dict")

        return HelperManager._prepare(df, "__author")

    @classmethod
    def _update_and_save(
        self,
        li: list,
        fn: str = "./data/base.csv",
    ) -> pd.DataFrame:
        """update base df and save updated df"""

        logging.debug("AuthorManager._update_and_save")

        _df = HelperManager._update_save(li, dest_key="_author", fn=fn)

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
        website="boiteachansons",
        nan_url="keep",
        top=10,
    ):
        """load data base using params and create __query column"""

        logging.debug("UrlManager._load_base")

        df = Loader.base(website=website, nan_url=nan_url, top=top)

        df.author.fillna("", inplace=True)
        df["__query"] = df.song + " " + df.author
        df["__query"] = df["__query"].str.strip()

        return df

    @classmethod
    def _scrap_urls(
        self,
        df: pd.DataFrame,
        asynch: bool = False,
    ):
        """scrap url with finder_url_manager"""

        logging.debug("UrlManager._scrap_urls")

        df = df.copy()
        df["__url"] = df["__query"].apply(
            lambda i: HelperManager._finder_url_manager(i)
        )

        # df["__url"] = df["__query"].parallel_apply(lambda i : _app(i))
        # df["__url"] = df["__query"].apply(_app)

        return df

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
        fn: str = "./data/base.csv",
        top: int = 10,
        n_sample: int = -1,
    ):
        """reload a entier base and update id / _url if neeeded, save final"""

        logging.debug("UrlManager._update_and_save")

        _df = HelperManager._update_save(li, dest_key="url", fn=fn)

        return _df

    @classmethod
    def run(
        self,
        top: int = 10,
        n_sample: int = -1,
        verbose: int = 1,
    ):
        """load, sample, scrap, prepare and update/save final"""

        logging.info("UrlManager.run")

        df = self._load_base(
            website="",
            nan_url="keep",
            top=top,
        )

        if not len(df):
            logging.warning(f"df empty : {len(df)} ")
            return 0

        df = HelperManager._sample(df, n_sample=n_sample)
        df = self._scrap_urls(df)
        li = self._prepare_list_dict(df)
        self._update_and_save(li)

        return 1


class DateManager:
    pass


class GeneratioManager:
    pass


class LangManager:
    pass


class StyleManager:
    pass


class PopManager:
    pass


class VideoManager:
    pass
