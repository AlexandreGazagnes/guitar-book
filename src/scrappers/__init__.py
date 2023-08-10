"""

"""

from src.scrappers.song_tab_scrapper import SongTabScrapper
from src.scrappers.song_video_scrapper import SongVideoScrapper
from src.scrappers.artist_bio_scrapper import ArtistBioScrapper


class SongScrapper:
    """Song Scrapper Class

    attributes:
        - video : class to scrap song video
        - tab : class to scrap song tab
    """

    video = SongVideoScrapper
    tab = SongTabScrapper


class ArtistScrapper:
    """Artist Scrapper Class

    attributes:
        - bio : class to scrap artist bio
    """

    bio = ArtistBioScrapper


class Scrapper:
    """Scrapper Class

    attributes:
        - song : class to scrap song
        - artist : class to scrap artist
    """

    song = SongScrapper
    artist = ArtistScrapper
