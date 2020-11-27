# -*- coding: utf-8 -*-
# @Author: Z.BOUDAOUD
# @Email: zinedddine97@gmail.com

import random
import requests
from bs4 import BeautifulSoup
from models.article import Article


class Maddyness:
    """
    Class used to store html code of a page at https://www.maddyness.com/
    """
    def __init__(self, url):
        html = requests.get(url).text
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_random_article(self):
        """Get a random article on the page
        :rtype: Article
        """
        links = self.soup.select(".article-img-link")
        random_index = random.randint(0, len(links) - 1)
        return Article(links[random_index].get('href'))
