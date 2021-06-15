import collections
import json
import re

import requests
from bs4 import BeautifulSoup


def request_link(url):
    """
    Requests the provided web page. Uses beautifulSoup to look for specific keys.
    :returns: links
    :rtype: list
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/74.0.3729.169 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, features='lxml')
    links = []

    for link in soup.findAll('a', class_='more-link', attrs={'href': re.compile("^https://")}):
        links.append(link.get('href'))

    return links


def concatenate_tags(content, number):
    text = ""
    for span in content[0:number]:
        text += span.get_text()

    return text


class WebScraper:
    def __init__(self, args):
        self.scraper = WebScraper
        self.url = args
        self.articlesList = []

    @staticmethod
    def request_content(url):
        """
        Requests the content of the provided url. Uses BeautifulSoup to look for specific keys.
        :returns: articles
        :rtype: list
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='lxml')
        return soup.find('main')

    def fill_data(self, links):
        """
        Takes BeautifulSoup produced list of links and looks for specific keys.
        Appends the dictionary a list
        """
        for link in links[0:20]:
            item = self.request_content(link)
            article = self.make_suitable_for_json(item)
            self.articlesList.append(article)

    @staticmethod
    def make_suitable_for_json(item):
        """
        Uses beautifulSoup instance to find specific content.
        Adds the found content to a dictionary.
        :returns: article
        :rtype: dict
        """

        title = item.find('h1', class_='entry-title').text
        date = item.find('time', class_='entry-date published').text
        content_list = item.findAll('span', attrs={'style': 'color:#000000;'})

        article = {
            'title': title.replace(' ', ' '),
            'date': date,
            'content': concatenate_tags(content_list, 3).replace(' ', ' ')
        }
        return article

    def write_to_json(self):
        """
        Takes the list of content.
        Uses json to convert the list to json file.
        """
        with open('./data/articles.json', 'w', encoding='utf-8') as file:
            json.dump(self.articlesList, file, ensure_ascii=False, indent=4)
        print("Saved to json file.")
