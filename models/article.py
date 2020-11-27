# -*- coding: utf-8 -*-
# @Author: Z.BOUDAOUD
# @Email: zinedddine97@gmail.com

import requests
from bs4 import BeautifulSoup

from models.company import Company


class Article:
    """
    Class used to store articles of https://www.maddyness.com/, and parse companies pages within them.
    """
    def __init__(self, url):
        html = requests.get(url).text
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_companies(self):
        """Parse html code of the article page and retrieve all companies pages.
        :return: Companies retrieved from the page
        :rtype: [Company]
        """
        company_links = self.soup.select('.financement-link')
        company_pages = []
        for link in company_links:
            company_pages.append(Company(link.get('href')))
        return company_pages
