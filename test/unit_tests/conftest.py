"""
Configuration for pytest.

NOTE: This file is automatically included when running pytest.
      There is no need to import it explicitly in the test files.
"""

import os
import sys
from pathlib import Path

import pytest

from scraper_app import WebScraper as WebScraper
from scraper_app import request_link as RequestLink


# allow the contents to be found automatically as if we were in that directory
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)


@pytest.fixture
def setup_scraper():
    _url = 'https://igicheva.wordpress.com/all-posts/'
    scraper = WebScraper(_url)
    scraper.articlesList = RequestLink(scraper.url)[0:2]

    return scraper


@pytest.fixture
def setup_test_data():
    fpath = Path('data/test_data.json').resolve()

    return fpath


@pytest.fixture
def setup_articles_data():
    fpath = Path('data/articles.json').resolve()

    return fpath



