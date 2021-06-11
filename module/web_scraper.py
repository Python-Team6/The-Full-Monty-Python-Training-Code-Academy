import json
import re
import requests
from bs4 import BeautifulSoup


def requestLink(url):
    """
    Requests the provided web page. Uses beautifulsoup to look for specific keys.
    :returns: links
    :rtype: list
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, features='lxml')
    links = []

    for link in soup.findAll('a', class_='more-link', attrs={'href': re.compile("^https://")}):
        links.append(link.get('href'))

    return links


class WebScraper:
    def __init__(self, args):
        self.scraper = WebScraper
        self.url = args
        self.articlesList = []

    def requestContent(self, url):
        """
        Requests the content of the provided url. Uses beautifulsoup to look for specific keys.
        :returns: articles
        :rtype: list
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='lxml')
        return soup.find('article')

    def fillData(self, links):
        """
        Takes beautifulsoup produced list of links and looks for specific keys.
        Appends the dictionary a list
        """
        for link in links[0:20]:
            item = self.requestContent(link)
            article = self.parse(item)
            self.articlesList.append(article)

    def parse(self, item):
        """
        Uses beautifulsoup instance to find specific content.
        Adds the found content to a dictionary.
        :returns: article
        :rtype: dict
        """
        title = item.find('h1', class_='entry-title').text
        date = item.find('time', class_='entry-date published').text

        content = ""
        contentList = item.findAll('span', attrs={'style': 'color:#000000;'})

        for span in contentList:
            content += span.get_text()

        article = {
            'title': title.replace(' ', ' '),
            'date': date,
            'content': content.replace(' ', ' ')
        }
        return article

    def output(self):
        """
        Takes the list of content.
        Uses json to convert the list to json file.
        """
        with open('./data/articles.json', 'w', encoding='utf-8') as file:
            json.dump(self.articlesList, file, ensure_ascii=False, indent=4)
        print("Saved to json file.")
