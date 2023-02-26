from dataclasses import dataclass, field
import bookmarks_parser


class Type:
    BOOKMARK = "bookmark"
    FOLDER = "folder"


@dataclass(unsafe_hash=True)
class Bookmark:
    name: str = field(compare=False)
    url: str


def _create_bookmarks(bookmarks: list[dict]) -> list[Bookmark]:
    return [
        Bookmark(name=bookmark["title"], url=bookmark["url"])
        for bookmark in bookmarks
        if bookmark["type"] == Type.BOOKMARK and "youtube.com" in bookmark["url"]
    ]


def parse_bookmarks(bookmarks_file_path: str, bookmarks_folder: str = None) -> list[Bookmark]:
    [bookmarks] = bookmarks_parser.parse(bookmarks_file_path)

    if bookmarks_folder is None:
        results = []

        for bookmark in bookmarks["children"]:
            if bookmark["type"] == Type.FOLDER and "musik" in bookmark["title"]:
                items = _create_bookmarks(bookmark["children"])
                for item in items:
                    if item not in results:
                        results.append(item)

        return results

    for bookmark in bookmarks["children"]:
        if bookmark["type"] == Type.FOLDER and bookmark["title"] == bookmarks_folder:
            return _create_bookmarks(bookmark["children"])

    return []
