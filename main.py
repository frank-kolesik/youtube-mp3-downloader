import argparse

from utils.downloader import download_mp3_from_bookmarks


def main() -> None:

    parser = argparse.ArgumentParser(description="Download Music From Youtube.")
    parser.add_argument("-p", help="path to bookmark file")
    parser.add_argument("-f", help="bookmark folder name")
    args = parser.parse_args()

    downloads = download_mp3_from_bookmarks(args.p, args.f)
    print(f"Number Of Downloads: {downloads}")


if __name__ == "__main__":

    main()
