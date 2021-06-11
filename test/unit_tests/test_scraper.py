import pytest
import json

from module import WebScraper as WebScraper
from module import requestLink as RequestLink
from main import some_helper
from bs4 import BeautifulSoup


@pytest.fixture
def web_scraper():
    url = 'https://igicheva.wordpress.com/all-posts/'
    scraper = WebScraper(url)
    scraper.url = url
    return scraper


def test_requestLink(web_scraper, links_list_fixture):
    test_links = links_list_fixture
    test_articles = RequestLink(web_scraper.url)
    assert test_articles[0:2] == test_links


def test_requestContent(web_scraper, links_list_fixture):
    test_soup = web_scraper.requestContent(links_list_fixture[0])
    assert isinstance(type(test_soup), type(BeautifulSoup)) == True
    assert test_soup is not None


def test_FillData(web_scraper):
    test_link = web_scraper.fillData(RequestLink(web_scraper.url))
    test_articleList = []
    test_articleList.append(test_link)
    assert test_articleList is not None


def test_parse(web_scraper, links_list_fixture):
    test_link = web_scraper.requestContent(links_list_fixture[0])
    test_article = web_scraper.parse(test_link)

    with open('data/test_data.json', 'r', encoding='utf-8') as file:
        test_output = json.load(file)

    assert test_article == test_output
    assert isinstance(type(test_article), type(dict)) == True


def test_output(web_scraper):
    assert web_scraper.output() is not FileNotFoundError


def test_webScraperClass(web_scraper):
    assert isinstance(web_scraper, WebScraper)
    assert web_scraper.scraper == WebScraper


def test_someFixture(links_list_fixture):
    assert links_list_fixture is not None


@pytest.mark.parametrize("input_arg", ["hi", "bye"])
def test_someHelper(input_arg):
    assert some_helper(input_arg) == f"I repeat: {input_arg}"
