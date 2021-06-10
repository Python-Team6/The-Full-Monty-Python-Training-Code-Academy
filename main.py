#!/usr/bin/env python3

import argparse

import module


def some_helper(argument):
    """Some echo-like helper function.

    Returns a string that contains the input argument.

    :param argument: the argument to print in the return string
    :type argument: any
    :returns: "I repeat: " followed by the input argument
    :rtype: str"""
    return f"I repeat: {argument}"


def parse_args():  # pragma: no cover
    """Parse the input args."""

    parser = argparse.ArgumentParser(
        description="Web scraper for wordpress based web sites."
    )

    parser.add_argument('-link',  type=str, required=True,
                        help='an link for scraping')

    return parser.parse_args()


def main(args):  # pragma: no cover
    """Main."""
    print(f"args: {args}")
    # print(f"RequestLink function result: {module.requestLink(args.link)}")
    scraper = module.WebScraper(args)
    links = module.requestLink(args.link)
    scraper.fillData(links)
    scraper.output()
    print(
        f"WebScraper class result:"
        f"\n - instance: {scraper}"
        f"\n - member:   {scraper.scraper}"
    )


if __name__ == "__main__":
    args = parse_args()
    some_helper(args)
    main(args)
