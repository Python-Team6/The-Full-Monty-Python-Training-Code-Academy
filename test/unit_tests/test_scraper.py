from scraper_app import *


# from scraper_app import request_link as RequestLink

# def setup(setup_scraper):
#     _url = 'https://igicheva.wordpress.com/all-posts/'
#     scraper = WebScraper(_url)
#     return scraper
# scraper = setup_scraper

def test_request_link(setup_scraper):
    test_articles = setup_scraper.request_link(setup_scraper.url)
    r_code = requests.get('https://furylabs.net/test')

    assert r_code.status_code != 200

    assert test_articles is not None
    assert test_articles[0:2] == setup_scraper.articlesList


def test_concatenate_tags(setup_scraper):
    test_string = "<span>cat</span> <span>dog</span> <span>eagle</span> <span>tiger</span>"
    soup = BeautifulSoup(test_string, features='lxml')
    test_content = soup.findAll("span")
    text_output = setup_scraper.concatenate_tags(test_content, 3)

    assert isinstance(type(text_output), type(str))
    assert text_output is not None


def test_get_comments_dict():
    test_authors = "<b>Tolkien</b> <b>Dog1</b> <b>Eagle1</b> <b>Tiger1</b>"
    soup = BeautifulSoup(test_authors, features='lxml')
    test_authors_names = soup.findAll("b")

    test_comments_content = "<div>Test1</div> <div>Test2</div> <div>Test3</div> <div>Test4</div>"
    soup = BeautifulSoup(test_comments_content, features='lxml')
    test_comments = soup.findAll("div")
    test_dict = setup_scraper.get_comments_dict(test_comments, test_authors_names)
    test_output = [{'Tolkien': 'Test1'},
                   {'Dog1': 'Test2'},
                   {'Eagle1': 'Test3'},
                   {'Tiger1': 'Test4'}]

    assert isinstance(type(test_dict), type(dict))
    assert test_dict is not None
    assert test_dict == test_output


def test_get_most_used_words():
    test_string = "cat dog eagle tiger bear tiger penguin seagull tiger"
    most_occur = setup_scraper.get_most_used_words(test_string)
    test_most_occur = ("tiger", 3)

    assert isinstance(type(most_occur), type(dict))
    assert most_occur is not None
    assert most_occur[0] == test_most_occur


def test_request_content(setup_scraper):
    test_soup = setup_scraper.request_content(setup_scraper.articlesList[0])
    test_other_blog_soup = setup_scraper.request_content('https://blog.bozho.net/blog/3733')

    assert isinstance(type(test_soup), type(BeautifulSoup))
    assert test_soup is not None

    assert test_soup != test_other_blog_soup


def test_fill_data(setup_scraper):
    test_link = setup_scraper.fill_data(setup_scraper.request_link(setup_scraper.url))
    test_article_list = [test_link]

    assert test_article_list is not None


def test_make_suitable_for_json(setup_scraper, setup_test_data):
    test_link = setup_scraper.request_content(setup_scraper.articlesList[0])
    test_article = setup_scraper.format_data_for_json(test_link)
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

    assert setup_scraper.write_to_json("test_articles") is not FileNotFoundError
    assert test_output is not None


def test_web_scraper_class(setup_scraper):
    assert isinstance(setup_scraper, WebScraper)


def test_setup(setup_scraper):
    assert setup_scraper.articlesList is not None
