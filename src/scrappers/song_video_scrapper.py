"""
"""

import requests
import logging

from googlesearch import search

from src.helpers import now
from pytube import YouTube
from typing import Optional

# import logging
# import time
# from bs4 import BeautifulSoup

# import time
# from googlesearch import search
# from src.threaders import ThreadManager


class SongVideoScrapper:
    """SongVideoScrapper
    ---- NOT IMPLEMENTED ----

    methods :
        - scrap : scrap song video"""

    @classmethod
    def scrap_save(
        self,
        url: str,
        song: str,
        artist: str,
    ) -> int:
        """ """

        _id = url.split("?v=")[1]
        dest = f"{artist}___{song}___"

        url = "https://www.youtube.com/watch?v=7Q6S19Vvh6s"
        url = "https://www.youtube.com/watch?v=GV85QI6NjM0"
        _id = url.split("?v=")[1]

        logging.critical("NOT IMPLEMENTED")

        yt = YouTube(url)
        streams = yt.streams.filter(only_audio=True)
        stream = streams[0]
        stream.download(path="./data/video", filename="coucou.mp4")

        return 1
