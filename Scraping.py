from bs4 import BeautifulSoup
import requests
import sys


class URL(object):

    def go(self):
        global soup
        chars = set('fishpond')
        r = requests.get(input("Please enter a Fishpond URL: "))
        if ((c in chars) for c in r) and r.status_code == 200:
            soup = BeautifulSoup(r.content, "lxml")
        else:
            print('Please enter a valid Fishpond URL')
            sys.exit(0)


class Webscraping(object):

    def product_name(self):
        product_name_results = []
        for product_name in soup.find_all("a", {"class": "blue_link fn url"}):
            try:
                product_name_results.append(product_name.text)
            except IndexError:
                print("No products found found")
        return product_name_results

    def isbn(self):
        isbn_results = []
        for isbn in soup.find_all("input", {"name": "barcode"}):
            try:
                isbn_results.append(isbn['value'])
            except IndexError:
                print("No ISBN valid found")
        return isbn_results

    def publishing_date(self):
        publishing_date_results = []
        for dates in soup.find_all("div", {"class": "productSearch-metainfo"}):
            try:
                publishing_date_results.append(dates.text.split(',', 1)[-1])
            except IndexError:
                print("No publishing dates found")
        return publishing_date_results

    def RRP(self):
        rrp_results = []
        for rrp in soup.find_all('s'):
            try:
                rrp_results.append(rrp.text[1:])
            except IndexError:
                print("No RRP found")
        return rrp_results

    def sale_prices(self):
        sale_price_results = []
        for salePrice in soup.find_all("span",
                                       {"class": "productSpecialPrice"}):
            try:
                sale_price_results.append(salePrice.text[1:])
            except IndexError:
                print("No sale prices found")
        return sale_price_results

    def saving_total(self):
        savings_results = []
        for savings in soup.find_all("span",
                                     {"class": "you_save"}):
            try:
                savings_results.append(savings.text.partition
                                       ('(')[-1].rpartition('%')[0])
            except IndexError:
                print("No savings found")
        return savings_results

    def photo_link(self):
        photo_link_results = []
        for photoLink in soup.find_all("img", {"class": "photo"}):
            try:
                photo_link_results.append(photoLink['src'])
            except IndexError:
                print("No photo links found")
        return photo_link_results
