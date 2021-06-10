"""
Configuration for pytest.

NOTE: This file is automatically included when running pytest.
      There is no need to import it explicitly in the test files.
"""

import os
import sys
import pytest
from module import requestLink as RequestLink

# allow the contents to be found automatically as if we were in that directory
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)


@pytest.fixture
def links_list_fixture():
    links_list = RequestLink('https://igicheva.wordpress.com/all-posts/')[0:2]
    return links_list
