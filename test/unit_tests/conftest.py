"""
Configuration for pytest.

NOTE: This file is automatically included when running pytest.
      There is no need to import it explicitly in the test files.
"""

import os
import sys
import pytest
from module import WebScraper as WebScraper
from module import request_link as RequestLink

# allow the contents to be found automatically as if we were in that directory
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)


@pytest.fixture
def setup():
    url = 'https://igicheva.wordpress.com/all-posts/'
    scraper = WebScraper(url)
    scraper.url = url
    links_list = RequestLink('https://igicheva.wordpress.com/all-posts/')[0:2]

