"""
loaders for db and files
"""

import os, logging
import pandas as pd


class Loader:
    """ """

    @classmethod
    def base(
        self,
        website: str,
        nan_url: str = None,
        not_processed: str = "only",
        top: int = 10,
    ) -> pd.DataFrame:
        """load base csv file

        Positionnal args:
            -
        Optional args:
            - website: str = "boiteachansons" or "ultimateguitar"
            - nan_url: str = None or "keep" or "drop" :
                keep : select only nan at url
                drop : drop nan at url
                None | 0 | False | "" : no filter
            - top: int = 10 : select n top rows
                < 0 | None | False : no filter
                1 > : select n top rows

        Returns:
            - df: pd.DataFrame of database base.csv
        """

        website_list = [
            "ultimate",
            "ultimate-guitar",
            "ultimateguitar",
            "boiteachansons",
            "boite",
            "bac",
            None,
            0,
            False,
            "",
        ]
        if isinstance(website, str):
            website = website.lower()
        if not website.lower() in website_list:
            raise AttributeError(
                f"website {website} not in website_list {website_list}"
            )

        if website:
            if "boite" in website:
                website = "boiteachansons"
            if "ultimate" in website:
                website = "ultimate-guitar"

        assert nan_url in ["", None, 0, False, "only", "drop", "ignore"]
        assert not_processed in ["", None, 0, False, "only", "drop", "ignore"]
        assert website in ["boiteachansons", ""]
        source = os.path.join(os.getcwd(), "data")
        fn = os.path.join(source, "base.csv")

        try:
            df = pd.read_csv(fn)
        except Exception as e:
            raise e

        logging.info(f"df.shape source loaded : {df.shape}")

        # select website
        if website:
            df = df.loc[df.website == website]
        logging.info(f"df.shape after {website}: {df.shape}")

        # keep only where url is nan
        if nan_url == "only":
            df = df.loc[df.url.isna()]
        # drop where url is nan
        elif nan_url == "drop":
            df = df.loc[df.url.notna()]
        logging.info(f"df.shape after nan_url == {nan_url}: {df.shape}")

        df.processed = df.processed.fillna(0).astype(int)
        if not_processed == "only":  # only not processed
            df = df.loc[df.processed < 1]
        elif not_processed == "drop":  # drop not processed :
            df = df.loc[df.processed > 0]
        logging.info(f"df.shape after not_processed == {not_processed}: {df.shape}")

        top = int(top) if top else -1
        if top > 0:
            df = df.iloc[:top]
        logging.info(f"df.shape after top {top} : {df.shape}")

        return df

    @classmethod
    def html_file_list(
        self,
        type_: str = "raw",
        website: str = "boiteachansons",
    ) -> list:
        """load list files of html docs"""

        html_list = os.listdir(os.path.join("data", type_, website))
        html_list = sorted(html_list)
        html_list = [i for i in html_list if i]
        html_list = [i for i in html_list if ".html" in i]

        return html_list
