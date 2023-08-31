class UrlCleaner:
    """ """

    @classmethod
    def author_song(self, url: str) -> str:
        """clean a utl str text to obtain a proper author song"""

        url = url.replace("-", " ").replace("+", " ")
        url = url.replace(".html", "")
        url = url.split("-chords-")[0]
        url = url.lower().strip().replace("  ", " ").replace("  ", " ").strip()

        return url
