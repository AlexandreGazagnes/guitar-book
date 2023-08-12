def clean_author_song_from_url(url: str) -> str:
    """ """

    url = url.replace("-", " ").replace("+", " ")
    url = url.replace(".html", "")
    url = url.split("-chords-")[0]
    url = url.lower().strip().replace("  ", " ").replace("  ", " ").strip()

    return url


def clean_chords_txt(i):
    """ """

    if not i:
        return None

    i = i.strip()
    i = i.replace("[", "").replace("]", "")
    if "love" in i.lower():
        return None
    if "refrain" in i.lower():
        return None
    return i
