# import youtube_dl
import yt_dlp  # fork of `youtube_dl`
import os

from .parser import parse_bookmarks


class System:
    DOCUMENTS = "~/Documents"
    DOWNLOADS = "~/Downloads"
    MUSIC = "~/Music"


def download_mp3_from_urls(
    webpage_urls: str | list[str],
    download_path: str = os.path.expanduser(System.DOWNLOADS),
) -> int:
    url_list = webpage_urls if type(webpage_urls) is list else [webpage_urls]
    options = {
        "outtmpl": download_path + "/%(title)s.%(ext)s",
        "format": "bestaudio",  # mp3/mp4/webm
        "noplaylist": True,
        "ignoreerrors": True,
        "keepvideo": False,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    youtube = yt_dlp.YoutubeDL(options)
    return youtube.download(url_list)


def download_mp3_from_bookmarks(
    bookmarks_file_path: str,
    bookmarks_folder: str = None,
    download_path: str = os.path.expanduser(System.DOWNLOADS),
) -> int:
    bookmarks = parse_bookmarks(bookmarks_file_path, bookmarks_folder)
    webpage_urls = [bookmark.url for bookmark in bookmarks]
    return download_mp3_from_urls(webpage_urls, download_path)
