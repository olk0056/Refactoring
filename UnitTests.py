import unittest
import re
from bs4 import BeautifulSoup
import requests
from Scraping import *

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
        self.assertTrue(Webscraping.product_name(self) == [])

    def test_isbn(self):
        self.assertTrue(Webscraping.isbn(self) == [])

    def test_date(self):
        self.assertTrue(Webscraping.publishing_date(self) == [])

    def test_rrp(self):
        self.assertTrue(Webscraping.RRP(self) == [])

    def test_sale(self):
        self.assertTrue(Webscraping.sale_prices(self) == [])

    def test_savings(self):
        self.assertTrue(Webscraping.saving_total(self) == [])

    def test_photo(self):
        self.assertTrue(Webscraping.photo_link(self) == [])