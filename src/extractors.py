import os, logging

from src.cleaners import clean_author_from_url


def extract_author_from_url(i: str) -> str:
    """helper function t oextract author from an url

    SHOULD BE IN AN EXTRACTOR MODULE
    """

    logging.info(i)

    if not isinstance(i, str):
        logging.error(f"{i} not a str : {type(i)}")
        return ""

    if not i:
        logging.error(f"{i} is null")
        return ""

    if not "/" in i:
        logging.error(f"/ not in i : {i}")
        return ""

    try:
        i = i.split("/")
        i = i[-2]

        i = clean_author_from_url(i)

        return i

    except Exception as e:
        logging.error(f"{e} ==> {i}")

        return ""
