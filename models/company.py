# -*- coding: utf-8 -*-
# @Author: Z.BOUDAOUD
# @Email: zinedddine97@gmail.com

import requests
from bs4 import BeautifulSoup


class Company:
    """
    Class used to store companies retrived from an article page on https://www.maddyness.com/
    """
    def __init__(self, page):
        self.page = page
        self.name = ""
        self.url = ""

    def get_infos(self):
        """Parse html code of the page and retrieve the name and website url of the company
        """
        html = requests.get(self.page).text
        company_soup = BeautifulSoup(html, 'html.parser')
        self.name = company_soup.h1.string
        self.url = company_soup.select_one(f'a[title$="{self.name}"]').get('href')

    def __str__(self):
        """Convert an object Company into a string
        """
        return f'{self.name}\t{self.url}'