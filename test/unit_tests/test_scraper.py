from module import *
from module import request_link as RequestLink
from bs4 import BeautifulSoup


def test_request_link(setup_scraper):
    test_articles = RequestLink(setup_scraper.url)
    r_code = requests.get('https://furylabs.net/test')

    assert r_code.status_code != 200

    assert test_articles is not None
    assert test_articles[0:2] == setup_scraper.articlesList

def test_concatenate_tags(set, number):
'''
def concatenate_tags(content, number):
    text = ""
    for span in content[0:number]:
        text += span.get_text()

    return text
'''

def test_request_content(setup_scraper):
    test_soup = request_content(setup_scraper.articlesList[0])
    test_other_blog_soup = request_content('https://blog.bozho.net/blog/3733')

    assert isinstance(type(test_soup), type(BeautifulSoup))
    assert test_soup is not None

    assert test_soup != test_other_blog_soup


def test_fill_data(setup_scraper):
    test_link = setup_scraper.fill_data(RequestLink(setup_scraper.url))
    test_article_list = [test_link]

    assert test_article_list is not None


def test_make_suitable_for_json(setup_scraper, setup_test_data):
    test_link = request_content(setup_scraper.articlesList[0])
    test_article = make_suitable_for_json(test_link)
    test_title = test_link.find('h1', class_='entry-title').text
    test_date = test_link.find('time', class_='entry-date published').text
    test_content_list = test_link.findAll('span', attrs={'style': 'color:#000000;'})

    path = setup_test_data

    with open(path, 'r', encoding='utf-8') as file:
        test_output = json.load(file)

    assert test_article == test_output
    assert isinstance(type(test_article), type(dict))

    assert isinstance(type(test_title), type(str))
    assert test_title is not None

    assert isinstance(type(test_date), type(str))
    assert test_date is not None

    assert isinstance(type(test_content_list), type(list))
    assert test_content_list is not None


def test_write_to_json(setup_scraper, setup_articles_data):
    path = setup_articles_data

    with open(path, 'r', encoding='utf-8') as file:
        test_output = json.load(file)

    assert setup_scraper.write_to_json() is not FileNotFoundError
    assert test_output is not None


def test_web_scraper_class(setup_scraper):

    assert isinstance(setup_scraper, WebScraper)


def test_setup(setup_scraper):

    assert setup_scraper.articlesList is not None
