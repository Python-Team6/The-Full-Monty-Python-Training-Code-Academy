import collections
import http
import json
import re
import unicodedata

import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, args):
        self.url = args
        self.articlesList = []

    def request_link(self, url):
        """
        Requests the provided web page. Uses beautifulSoup to look for specific keys.
        :returns: links
        :rtype: list
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                          'Chrome/74.0.3729.169 Safari/537.36'}

        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        soup = BeautifulSoup(r.content, features='lxml')
        links = []

        for link in soup.findAll('a', class_='more-link', attrs={'href': re.compile("^https://")}):
            links.append(link.get('href'))

        return links

    def fill_data(self, links):
        """
        Takes BeautifulSoup produced list of links and looks for specific keys.
        Appends the dictionary a list
        """
        for link in links[0:20]:
            item = self.request_content(link)
            article = self.format_data_for_json(item)
            self.articlesList.append(article)

    def request_content(self, url):
        """
        Requests the content of the provided url. Uses BeautifulSoup to look for specific keys.
        :returns: articles
        :rtype: list
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='lxml')

        return soup.find('main')

    def format_data_for_json(self, item):
        """
        Uses beautifulSoup instance to find specific content.
        Adds the found content to a dictionary.
        :returns: article
        :rtype: dict
        """

        title = item.find('h1', class_='entry-title').text
        title = unicodedata.normalize("NFKD", title)
        date = item.find('time', class_='entry-date published').text
        date = unicodedata.normalize("NFKD", date)
        content_list = item.findAll('span', attrs={'style': 'color:#000000;'})
        comments = item.findAll('div', class_='comment-content')
        authors_list = item.findAll('b', class_='fn')

        article = {
            'title': title,
            'date': date,
            'content': self.append_tags(content_list, 3),
            'most_used_words': dict(self.get_most_used_words(self.concatenate_tags(content_list, None))),
            'comments': self.get_comments_dict(comments, authors_list)
        }

        return article

    def append_tags(self, content, number):
        """
        Takes beautifulSoup content and the number of elements to concatenate.
        :returns: text
        :rtype: str
        """
        text = []
        for span in content[0:number]:
            text.append(span.get_text())

        return text

    def get_most_used_words(self, full_content):
        """
        Takes string content. Splits it to a list. Finds the three most common words.
        :returns: most_occur
        :rtype: list[tuple]
        """
        min_length_words = []
        split_it = full_content.split()
        for word in split_it:
            if len(word) > 4:
                min_length_words.append(word)
        all_words = collections.Counter(min_length_words)

        most_occur = all_words.most_common(3)

        return most_occur

    def concatenate_tags(self, content, number):
        """
        Takes beautifulSoup content and the number of elements to concatenate.
        :returns: text
        :rtype: str
        """
        text = ""
        for span in content[0:number]:
            text += span.get_text()

        return text

    def get_comments_dict(self, comments, authors_list):
        """
        Takes beautifulSoup comments and authors_list. Combines them into a dictionary. Reverses the resulting dictionary.
        :returns: reversed_dict
        :rtype: dict
        """
        j = 0
        auth_comment_dict = []
        for i in comments:
            auth_comment_dict.append({authors_list[j].get_text(): i.get_text().replace('\n', '')})
            j += 1

        return auth_comment_dict

    def write_to_json(self, file_name):
        """
        Takes the list of content.
        Uses json to convert the list to json file.
        """

        with open(f'data/{file_name}.json', 'w', encoding='utf-8') as file:
            json.dump(self.articlesList, file, ensure_ascii=False, indent=4)
        print("Saved to json file.")
