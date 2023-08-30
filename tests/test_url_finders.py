import pytest

from src.loggers import create_logger

from src.url_finders import UrlFinder
import logging

create_logger()


ultimate = [
    ("alphonse brown mickael young", "", "ultimate", -1),
    ("3-0 ogres de barback", "", "ultimateguitar", -1),
    ("la corrida", "cabrel", "ultimate-guitar", -1),
]

boite = [
    ("alphonse brown mickael young", "", "boiteachansons", -1),
    ("3-0 ogres de barback", "", "boite", -1),
    ("la corrida", "cabrel", "bac", -1),
]


#########################################
#       ADD STATUS CODE VALIDATION
#########################################


class TestUrlFinders:
    @pytest.mark.parametrize("name,author,website,status", ultimate)
    def test_ultimate(self, name, author, website):
        """ """

        response = UrlFinder.song.robust_tab(
            name,
            author=author,
            website=website,
        )
        logging.warning(response)


@pytest.mark.parametrize("name,author,website", boite)
def test_boite(self, name, author, website):
    """ """

    response = UrlFinder.song.robust_tab(
        name,
        author=author,
        website=website,
    )
    logging.warning(response)
