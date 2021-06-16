
import pytest
import requests

from module import *
from module import request_link as RequestLink
from bs4 import BeautifulSoup


def test_request_link(setup):
    test_articles = RequestLink(setup.url)
    r_code = requests.get('https://furylabs.net/test')

    assert r_code.status_code != 200

    assert test_articles is not None
    assert test_articles[0:2] == setup.articlesList


def test_request_content(setup):
    test_soup = setup.request_content(setup.articlesList[0])
    test_other_blog_soup = setup.request_content('https://blog.bozho.net/blog/3733')

    assert isinstance(type(test_soup), type(BeautifulSoup))
    assert test_soup is not None

    assert test_soup != test_other_blog_soup


def test_fill_data(setup):
    test_link = setup.fill_data(RequestLink(setup.url))
    test_article_list = [test_link]
    assert test_article_list is not None

def test_make_suitable_for_json(setup):
    test_link = setup.request_content(setup.articlesList[0])
    test_article = setup.make_suitable_for_json(test_link)
    test_title = test_link.find('h1', class_='entry-title').text
    test_date = test_link.find('time', class_='entry-date published').text
    test_content_list = test_link.findAll('span', attrs={'style': 'color:#000000;'})

    with open('/home/vhunterd/Projects/The-Full-Monty-Python-Training-Code-Academy/data/test_data.json', 'r',
              encoding='utf-8') as file:
        test_output = json.load(file)

    assert test_article == test_output
    assert isinstance(type(test_article), type(dict))

def test_write_to_json(setup):
    with open('/home/vhunterd/Projects/The-Full-Monty-Python-Training-Code-Academy/data/articles.json', 'r',
              encoding='utf-8') as file:
        test_output = json.load(file)

    assert setup.write_to_json() is not FileNotFoundError
    assert test_output is not None


def test_web_scraper_class(setup):
    assert isinstance(setup, WebScraper)


def test_setup(setup):
    assert setup.articlesList is not None
