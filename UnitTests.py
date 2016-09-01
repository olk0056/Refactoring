import unittest
import re
from bs4 import BeautifulSoup
import requests
from Scraping import Webscraping


class Scraping_Test(unittest.TestCase):
    def test_Soup(self):
        """testing output of soup scraping using original method"""
        r = requests.get("http://www.fishpond.co.nz/Books/Fiction_Literature")
        soup = BeautifulSoup(r.content, "lxml")
        rrp_results = []
        for rrp in soup.find_all('s'):
            try:
                rrp_results.append(rrp.text[1:])
            except IndexError:
                print("No RRP found")
        self.assertTrue(len(rrp_results) != 0)


    def test_name(self):
        '''
        Testing code of string formatter for validity, hardcoded as url is usually set through CMD before running
        '''
        r = requests.get("http://www.fishpond.co.nz/Books/Fiction_Literature")
        soup = BeautifulSoup(r.content, "lxml")
        product_name_results = []
        name = '("string1", {"string2": "string3"}).format(string1="a", string2="class", string3="blue_link fn url")'
        for product_name in soup.find_all(name):
            try:
                product_name_results.append(product_name.text)
            except IndexError:
                print("No products found found")
        return product_name_results
        self.assertTrue(len(Webscraping.product_name(self)) != 0)