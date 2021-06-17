import argparse
import module


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
    scraper = module.WebScraper(args)
    links = module.request_link(args.link)
    scraper.fill_data(links)
    scraper.write_to_json()

    print(
        f"WebScraper class result:"
        f"\n - instance: {scraper}"
        f"\n - member:   {scraper.scraper}"
    )


if __name__ == "__main__":
    args = parse_args()
    main(args)
