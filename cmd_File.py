import cmd
from scraping import *
import pickle
import os
from Data_Methods import Data_Methods


class HelpCMD(cmd.Cmd, Webscraping):

    """
    Web Scraping CMD
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
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
            print("Product name: ", Webscraping.product_name(self))
            print("ISBN:  ", Webscraping.isbn(self))
            print('Publishing Date: ', Webscraping.publishing_date(self))
            print('RRP ($): ', Webscraping.RRP(self))
            print('Sale Price ($): ', Webscraping.sale_prices(self))
            print('Savings : ', Webscraping.saving_total(self))
            print('Product Photo: ', Webscraping.photo_link(self))
        except NameError:
            print("Please set a url")

    def do_product(self, webscraping):
        """
        List of all scraped product names, as list
         """
        try:
            print("Product name: ", Webscraping.product_name(self))
        except NameError:
            print("Please set a url")

    def do_isbn(self, webscraping):
        """
        List of all scraped product ISBN's, as list
        """
        try:
            print("ISBN:  ", Webscraping.isbn(self))
        except NameError:
            print("Please set a url")

    def do_savings(self, webscraping):
        """
        List of all scraped savings, as list
        """
        try:
            print('Savings : ', Webscraping.saving_total(self))
        except NameError:
            print("Please set a url")

    def do_publish(self, webscraping):
        """
        List of all scraped product's Publishing Date, as list
        """
        try:
            print('Publishing Date: ', Webscraping.publishing_date(self))
        except NameError:
            print("Please set a url")

    def do_rrp(self, webscraping):
        """
        List of all scraped product RRP, as list
        """
        try:
            print('Normal Price ($): ', Webscraping.RRP(self))
        except NameError:
            print("Please set a url")

    def do_sale(self, webscraping):
        """
        List of all scraped product's Sale Price, as list
        """
        try:
            print('Sale Price ($): ', Webscraping.sale_prices(self))
        except NameError:
            print("Please set a url")

    def do_image(self, webscraping):
        """
        List of all scraped product's relevant image, as url list
        """
        try:
            print('Product Photo: ', Webscraping.photo_link(self))
        except NameError:
            print("Please set a url")

    def do_pricecomparison(self, webscraping):
        """
        Graphical comparison of RRP and Sale Price for all products
        """
        try:
            Data_Methods.price_comparison(self)
        except NameError:
            print("Please set a url")

    def do_totalsavingsdata(self, webscraping):
        """
        Graph showing the savings (%) of all the products scraped
        """
        try:
            Data_Methods.total_savings_data(self)
        except NameError:
            print("Please set a url")

    def do_publishingdata(self, webscraping):
        """
        Pie chart showing a breakdown publishing dates by month
        """
        try:
            Data_Methods.publishing_data(self)
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
            results = Webscraping()
            save_path = input("What is the directory?: ")
            try:
                name_of_file = input("What is the name of the file: ")
                type = input("What data type do you want to save?: ")
                if type == 'Product Name':
                    save = results.product_name()
                elif type == 'ISBN':
                    save = results.isbn()
                elif type == "Publish Date":
                    save = results.publishing_date()
                elif type == 'Normal Price':
                    save = results.RRP()
                elif type == 'Sale Price':
                    save = results.sale_prices()
                elif type == 'Savings':
                    save = results.saving_total()
                elif type == 'Photos':
                    save = results.photo_link()
                elif type == "Save all":
                    save = (results.product_name(), results.isbn(), results.RRP(),
                            results.sale_prices(),
                            results.saving_total(), results.photo_link())
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