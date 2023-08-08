def clean_author_from_url(i):
    """ """

    i = i.replace("-", " ")
    i = i.lower().strip()

    return i


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
