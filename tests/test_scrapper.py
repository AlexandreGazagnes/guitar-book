import pytest


from src.scrappers import UrlFinder


LI = [
    (
        "boiteachansons",
        "la corrida",
        "https://www.boiteachansons.net/partitions/francis-cabrel/la-corrida",
        True,
    ),
    (
        "",
        "firework katy perry",
        None,
        False,
    ),
]


@pytest.mark.parametrize("webiste,query,url,should_find", LI)
def test_UrlFinder_song_tab(webiste, query, url, should_find):
    """ """

    ans_list = UrlFinder.song_tab(query, website=webiste)

    if should_find:
        assert ans_list[0] == url
    else:
        assert len(ans_list) == 0
