import pytest


from src.url_finders import UrlFinder


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
    (
        "boiteachansons",
        "Samba do Brésil Bellini",
        None,
        False,
    ),
]


@pytest.mark.parametrize("webiste,query,url,should_find", LI)
def test_UrlFinder_song_tab(webiste, query, url, should_find):
    """ """

    results = UrlFinder.song_tab(
        query,
        website=webiste,
        tab="tab",
        limit=10,
    )

    assert results

    if should_find:
        assert results["url_list"][0] == url
    else:
        assert len(results["url_list"]) == 0
