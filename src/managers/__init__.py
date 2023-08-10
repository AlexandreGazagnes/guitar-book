"""
Managers modules
"""


from src.managers.url_manager import UrlManager
from src.managers.author_manager import AuthorManager


class DateManager:
    """NOT IMPLEMENTED"""

    pass


class GeneratioManager:
    """NOT IMPLEMENTED"""

    pass


class LangManager:
    """NOT IMPLEMENTED"""

    pass


class StyleManager:
    """NOT IMPLEMENTED"""

    pass


class PopManager:
    """NOT IMPLEMENTED"""

    pass


class VideoManager:
    """NOT IMPLEMENTED"""

    pass


class Manager:
    url = UrlManager
    author = AuthorManager
    date = DateManager
    generation = GeneratioManager
    lang = LangManager
    style = StyleManager
    pop = PopManager
    video = VideoManager
