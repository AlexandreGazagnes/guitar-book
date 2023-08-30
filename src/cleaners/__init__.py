from src.cleaners.text_cleaner import TextCleaner
from src.cleaners.url_cleaner import UrlCleaner


class Cleaner:
    """
    Cleaner class

    Attributes:
        - text | txt : text cleaners
        - url : url cleaners
    """

    text = TextCleaner
    txt = TextCleaner
    url = UrlCleaner
