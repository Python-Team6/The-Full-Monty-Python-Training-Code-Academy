import argparse
import scraper_app


def parse_args():  # pragma: no cover
    """Parse the input args."""

    parser = argparse.ArgumentParser(
        description="Web scraper for wordpress based web sites."
    )

    parser.add_argument('-link', type=str, required=True,
                        help='an link for scraping')

    return parser.parse_args()


def main(args):  # pragma: no cover
    """Main."""
    print(f"args: {args}")
    scraper = scraper_app.WebScraper(args)
    links = scraper.request_link(args.link)
    scraper.fill_data(links)
    scraper.write_to_json("articles")


if __name__ == "__main__":
    args = parse_args()
    main(args)
