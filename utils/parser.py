from dataclasses import dataclass
import bookmarks_parser


class Type:
    BOOKMARK = "bookmark"
    FOLDER = "folder"


@dataclass
class Bookmark:
    name: str
    url: str


def _create_bookmarks(bookmarks: list[dict]) -> list[Bookmark]:
    return [
        Bookmark(name=bookmark["title"], url=bookmark["url"])
        for bookmark in bookmarks
        if bookmark["type"] == Type.BOOKMARK
    ]


def parse_bookmarks(
    bookmarks_file_path: str, bookmarks_folder: str = None
) -> list[Bookmark]:
    [bookmarks] = bookmarks_parser.parse(bookmarks_file_path)

    if bookmarks_folder is None:
        return _create_bookmarks(bookmarks["children"])

    for bookmark in bookmarks["children"]:
        if bookmark["type"] == Type.FOLDER and bookmark["title"] == bookmarks_folder:
            return _create_bookmarks(bookmark["children"])

    return []
