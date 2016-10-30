import cmd
import pickle
import os
from Data_Method import *
from datetime import datetime
import scraping
import graphing as graphs

class HelpCMD(cmd.Cmd, Webscraping):

    """
    Web Scraping CMD
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        args = sys.argv[1:]
        if args:
            for arg in args:
                if arg == 'Time':
                    print("Starting at", datetime.now()
                          .strftime('%Y-%m-%d %H:%M:%S'))
                    self.prompt = ">>>"
                    self.cmdloop()
        else:
            self.prompt = ">>>"
            self.cmdloop()

    def do_seturl(self, url):
        """
        Set URL of Fishpond page to scrap information from
        :return: Input
         """
        URL.go(self)

    def do_printall(self, webscraping):
        """
        List of all scraped data, as list
        """
        try:
            self.do_product(webscraping)
            self.do_isbn(webscraping)
            self.do_publish(webscraping)
            self.do_rrp(webscraping)
            self.do_sale(webscraping)
            self.do_savings(webscraping)
            self.do_image(webscraping)
        except NameError:
            print("Please set a url")

    def do_product(self, webscraping):
        """
        List of all scraped product names, as list
         """
        try:
            scraper = scraping.Director()
            scraper.builder = scraping.product_name()
            product = scraper.create2()
            print("Product Name: ", product.temp2())
        except NameError:
            print("Please set a url")

    def do_isbn(self, webscraping):
        """
        List of all scraped product ISBN's, as list
        """
        try:
            scraper = scraping.Director()
            scraper.builder = scraping.isbn()
            temp = scraper.create()
            print("ISBN: ", temp.temp())
        except NameError:
            print("Please set a url")

    def do_savings(self, webscraping):
        """
        List of all scraped savings, as list
        """
        try:
            scraper = scraping.Director()
            scraper.builder = scraping.saving_total()
            savings = scraper.create2()
            results = savings.temp2()
            myList = [i.partition('(')[-1].rpartition('%')[0] for i in results]
            print('Savings : ', myList)
        except NameError:
            print("Please set a url")

    def do_publish(self, webscraping):
        """
        List of all scraped product's Publishing Date, as list
        """
        try:
            scraper = scraping.Director()
            scraper.builder = scraping.publishing_date()
            publish = scraper.create2()
            results = publish.temp2()
            myList = [i.split(',', 1)[-1].strip() for i in results]
            print('Publishing Date', myList)
        except NameError:
            print("Please set a url")

    def do_rrp(self, webscraping):
        """
        List of all scraped product RRP, as list
        """
        try:
            scraper = scraping.Director()
            scraper.builder = scraping.RRP()
            rrp = scraper.create2()
            results = rrp.temp2()
            myList = [i[1:] for i in results]
            print("Recommended retail price ($)", myList)
        except NameError:
            print("Please set a url")

    def do_sale(self, webscraping):
        """
        List of all scraped product's Sale Price, as list
        """
        try:
            scraper = scraping.Director()
            scraper.builder = scraping.sale_prices()
            sale = scraper.create2()
            results = sale.temp2()
            myList = [i[1:] for i in results]
            print('Sale Price ($): ',myList)
        except NameError:
            print("Please set a url")

    def do_image(self, webscraping):
        """
        List of all scraped product's relevant image, as url list
        """
        try:
            scraper = scraping.Director()
            scraper.builder = scraping.photo_link()
            photo = scraper.create()
            print('Product Photo: ', photo.temp())
        except NameError:
            print("Please set a url")

    def do_pricecomparison(self, webscraping):
        """
        Graphical comparison of RRP and Sale Price for all products
        """
        try:
            graphing = graphs.GrapherFactory()
            graphing.get_graph("Price")
        except NameError:
            print("Please set a url")

    def do_totalsavingsdata(self, webscraping):
        """
        Graph showing the savings (%) of all the products scraped
        """
        try:
            graphing = graphs.GrapherFactory()
            graphing.get_graph("Savings")
        except NameError:
            print("Please set a url")

    def do_publishingdata(self, webscraping):
        """
        Pie chart showing a breakdown publishing dates by month
        """
        try:
            graphing = graphs.GrapherFactory()
            graphing.get_graph("Data")
        except NameError:
            print("Please set a url")

    def do_quit(self, webscraping):
        """
        Quit from my CMD
        """
        print("Quitting ......")
        return True

    def help_quit(self, webscraping):
        print('\n'.join(['Quit from my CMD', ':return: True']))

    def do_savefile(self, webscraping):
        """
        Saves information scraped to txt file
        :data types: Product Name, ISBN, Publish Date, Normal Price,
                    Sale Price, Savings, Photos, All
        """
        try:
            save_path = input("What is the directory?: ")
            try:
                name_of_file = input("What is the name of the file: ")
                type = input("What data type do you want to save?: ")
                if type == 'Product Name':
                    save = self.do_product(webscraping)
                elif type == 'ISBN':
                    save = self.do_isbn(webscraping)
                elif type == "Publish Date":
                    save = self.do_publish(webscraping)
                elif type == 'Normal Price':
                    save = self.do_rrp(webscraping)
                elif type == 'Sale Price':
                    save =  self.do_sale(webscraping)
                elif type == 'Savings':
                    save = self.do_savings(webscraping)
                elif type == 'Photos':
                    save = self.do_image(webscraping)
                elif type == "Save all":
                    save = (self.do_product(webscraping), self.do_isbn(webscraping),self.do_publish(webscraping),
                    self.do_rrp(webscraping), self.do_sale(webscraping), self.do_savings(webscraping), self.do_image(webscraping))
                complete_name = os.path.join(save_path, name_of_file + ".txt")
                file1 = open(complete_name, "wb")
                pickle.dump(save, file1)
                file1.close()
            except FileNotFoundError:
                    print("Please enter a valid save directory")
        except NameError:
            print("Please set a url")

    def do_loadfile(self, webscraping):
        """
        Loads data from previously saved file
        """
        infile = input("Please enter the file path: ")
        try:
            f = open(infile, 'rb')
            results = pickle.load(f)
            print(results)
            f.close()
        except FileNotFoundError:
            print("Please enter a valid file path")

if __name__ == '__main__':
    prompt = HelpCMD()

