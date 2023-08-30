import pytest
import logging

from src.loggers import create_logger
from src.cleaners import Cleaner

create_logger()


none = [
    # moche # clean # authorise_none # expect_error
    ("", None, False, True),
    (0, None, False, True),
    (False, None, False, True),
    (None, None, False, True),
]

boite = [
    # moche # clean # authorise_none # expect_error
    ("boite", "boiteachansons", True, False),
    ("bac", "boiteachansons", True, False),
    ("boiteachansons", "boiteachansons", True, False),
]


ultimate = [
    # moche # clean # authorise_none # expect_error
    ("ultimate", "ultimate-guitar", True, False),
    ("ulimate-guitar", "ultimate-guitar", True, False),
    ("ultimateguitar", "ultimate-guitar", True, False),
]


class TestValidators:
    """ """

    @pytest.mark.parametrize("website,authorise_none,expect_error", ultimate)
    def test_tab_website_ultimate(self, website, authorise_none, expect_error):
        if expect_error:
            with pytest.raises(Exception):
                Cleaner.txt.tab_website(website, authorise_none=authorise_none)

        else:
            Cleaner.txt.tab_website(website, authorise_none=authorise_none)
