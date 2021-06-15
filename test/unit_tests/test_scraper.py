import pytest

from module import *
from module import request_link as RequestLink
from bs4 import BeautifulSoup

url = 'https://igicheva.wordpress.com/all-posts/'
scraper = WebScraper(url)
links_list = RequestLink('https://igicheva.wordpress.com/all-posts/')[0:2]


def test_request_link():
    test_articles = RequestLink(scraper.url)
    assert test_articles[0:2] == links_list


def test_request_content():
    test_soup = scraper.request_content(links_list[0])
    assert isinstance(type(test_soup), type(BeautifulSoup))
    assert test_soup is not None


def test_fill_data():
    test_link = scraper.fill_data(RequestLink(scraper.url))
    test_article_list = [test_link]
    assert test_article_list is not None


def test_make_suitable_for_json():
    test_link = scraper.request_content(links_list[0])
    test_article = scraper.make_suitable_for_json(test_link)

    with open('data/test_data.json', 'r', encoding='utf-8') as file:
        test_output = json.load(file)

    assert test_article == test_output
    assert isinstance(type(test_article), type(dict))


def test_write_to_json():
    assert scraper.write_to_json() is not FileNotFoundError


def test_webScraperClass():
    assert isinstance(scraper, WebScraper) == True



def test_someFixture():
    assert links_list is not None


