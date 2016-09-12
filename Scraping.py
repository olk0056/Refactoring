from bs4 import BeautifulSoup
import requests
import sys

'''
class URL(object):

  def go(self):
        global soup
        chars = set('fishpond')
        r = requests.get(input("Please enter a Fishpond URL: "))
        if ((c in chars) for c in r) and r.status_code == 200:
            soup = BeautifulSoup(r.content, "lxml")
        else:
            print('Please enter a valid Fishpond URL')
            sys.exit(0)'''

class Webscraping(object):
    global soup
    r = requests.get("http://www.fishpond.co.nz/Books/Fiction_Literature")
    soup = BeautifulSoup(r.content, "lxml")

    def temp(span, classes, specific, appends):
        result = []
        for x in soup.find_all(span, {classes: specific}):
            try:
                result.append(x[appends])
            except IndexError:
                print("No products found found")
        return result


    def temp2(span, classes, specific):
        result = []
        for x in soup.find_all(span, {classes: specific}):
            try:
                result.append(x.text)
            except IndexError:
                print("No products found found")
        return result

    def product_name(self):
        return(Webscraping.temp2("a", "class", "blue_link fn url"))

    def isbn(self):
        return(Webscraping.temp("input", "name", "barcode", "value"))

    def publishing_date(self):
        results = Webscraping.temp2('div', "class", "productSearch-metainfo")
        myList = [i.split(',', 1)[-1].strip() for i in results]
        return(myList)

    def RRP(self):
        results = Webscraping.temp2("s", "", "")
        myList = [i[1:] for i in results]
        return(myList)

    def sale_prices(self):
        results = Webscraping.temp2("span", "class", "productSpecialPrice")
        myList = [i[1:] for i in results]
        return(myList)

    def saving_total(self):
        results = Webscraping.temp2('span', "class", "you_save")  # savings
        myList = [i.partition('(')[-1].rpartition('%')[0] for i in results]
        return(myList)

    def photo_link(self):
        return(Webscraping.temp("img", "class", "photo", "src"))  # photo
