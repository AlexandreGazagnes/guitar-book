"""
"""

import requests
import logging
import time

from googlesearch import search

from src.helpers import now
from pytube import YouTube
from typing import Optional

# import logging
# from bs4 import BeautifulSoup

# import time
# from googlesearch import search
# from src.threaders import ThreadManager


class SongVideoScrapper:
    """SongVideoScrapper

    methods :
        - scrap_save : scrap song video"""

    @classmethod
    def scrap_save(
        self,
        url: str,
        song: str,
        author: str,
        live: str = "",
        album: str = "",
        path="./data/video/",
    ) -> int:
        """ """

        t0 = time.time()
        t1 = -1

        dd = {
            "song": song,
            "author": author,
            "path": path,
            "date": now(),
            "url": url,
            "live": live,
            "album": album,
        }

        # dd
        try:
            _id = url.split("?v=")[1]
            _now = now(replace_space="_")
            filename = f"{author}___{song}___{_id}___{_now}.mp3"
        except Exception as e:
            response = {"status": 500, "comment": e, "time": time.time() - t0}
            response.update(dd)
            logging.error(response)
            return response

        # yt
        try:
            yt = YouTube(url)
        except Exception as e:
            response = {"status": 501, "comment": e, "time": time.time() - t0}
            response.update(dd)
            logging.error(response)
            return response

        # filter
        try:
            streams = yt.streams.filter(only_audio=True)
        except Exception as e:
            response = {"status": 502, "comment": e, "time": time.time() - t0}

            response.update(dd)
            logging.error(response)
            return response

        # first stream
        try:
            stream = streams[0]
        except Exception as e:
            response = {"status": 503, "comment": e, "time": time.time() - t0}
            response.update(dd)
            logging.error(response)
            return response

        # dl
        try:
            out = stream.download(output_path=path, filename=filename, timeout=15)
        except Exception as e:
            response = {"status": 504, "comment": e, "time": time.time() - t0}
            response.update(dd)
            logging.error(response)
            return response

        # else
        response = {
            "status": 200,
            "comment": "OK",
            "_id": _id,
            "filename": filename,
            "time": time.time() - t0,
        }
        response.update(dd)
        logging.info(response)
        return response


# if __name__ == "__main__":
#     import requests
#     import logging

#     from googlesearch import search

#     from src.helpers import now
#     from pytube import YouTube
#     from typing import Optional

#     # li
#     li = [
#         {
#             "_song": "99 luftballons",
#             "_author": "nena",
#             "url_video": "https://www.youtube.com/watch?v=Fpu5a0Bl8eY",
#         },
#         {
#             "_song": "a nos souvenirs",
#             "_author": "trois cafes gourmands",
#             "url_video": "https://www.youtube.com/watch?v=voQhp1K2TSk",
#         },
#         {
#             "_song": "adieu cher camarade",
#             "_author": "marc ogeret",
#             "url_video": "https://www.youtube.com/watch?v=lftrgBS8kn0",
#         },
#         {
#             "_song": "africa",
#             "_author": "toto",
#             "url_video": "https://www.youtube.com/watch?v=FTQbiNvZqaY",
#         },
#         {
#             "_song": "ah le petit vin blanc",
#             "_author": "lina margy",
#             "url_video": "https://www.youtube.com/watch?v=IDmPxv3hUaI",
#         },
#         {
#             "_song": "aimer est plus fort que d etre aime",
#             "_author": "daniel balavoine",
#             "url_video": "https://www.youtube.com/watch?v=6bTAgC-1Brs",
#         },
#         {
#             "_song": "alexandrie alexandra",
#             "_author": "claude francois",
#             "url_video": "https://www.youtube.com/watch?v=HkVhN64dyd8",
#         },
#         {
#             "_song": "allez reste",
#             "_author": "boulevard des airs",
#             "url_video": "https://www.youtube.com/watch?v=lM3R1vkb21s",
#         },
#         {
#             "_song": "allumer le feu",
#             "_author": "johnny hallyday",
#             "url_video": "https://www.youtube.com/watch?v=s3O1Xro7oAI",
#         },
#         {
#             "_song": "amsterdam",
#             "_author": "jacques brel",
#             "url_video": "https://www.youtube.com/watch?v=V3BSj1cHX-M",
#         },
#     ]

#     # song

#     author = li[0]["_author"]
#     song = li[0]["_song"]
#     url = li[0]["url_video"]
#     _id = url.split("?v=")[1]
#     dest = f"{author}___{song}___{_id}.mp3"
