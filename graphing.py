import scraping
import re
from matplotlib import pyplot as plt

class Grapher(object):
    def build_graph(self, para):
        raise NotImplementedError

    def get_graph(self, para):
        graph = self.build_graph(para)
        return graph.do_use()


class GrapherFactory(Grapher):
    def build_graph(self, para):
        if para == "Data":
            return DataGraph()
        if para == "Price":
            return PriceGraph()
        if para == "Savings":
            return SavingsGraph()

        return None


class Graphs(object):
    def do_use(self):
        raise NotImplementedError


class DataGraph(Graphs):
    def do_use(self):
        months = ['January', 'February', 'March', 'April', 'May',
                  'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

        global month_list
        scraper = scraping.Director()
        scraper.builder = scraping.publishing_date()
        publish = scraper.create2()
        results = publish.temp2()
        myList = [i.split(',', 1)[-1].strip() for i in results]

        month_list = [[], [], [], [], [], [], [], [], [], [], [], []]

        x = 0
        while x <= 11:
            for strings in myList:
                if strings == months[x]:
                    month_list[x].append(1)
            x += 1

        # Data to plot
        labels = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October',
                  'November', 'December']
        sizes = [len(month_list[0]), len(month_list[1]), len(month_list[2]),
                 len(month_list[3]), len(month_list[4]), len(month_list[5]),
                 len(month_list[6]), len(month_list[7]), len(month_list[8]),
                 len(month_list[9]), len(month_list[10]), len(month_list[11])]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue',
                  'red', 'black', 'blue', 'yellow', 'green',
                  'purple', 'orange', 'darkblue']
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)

        plt.axis('equal')
        plt.show()

class PriceGraph(Graphs):
    def do_use(self):
            x = []
            count = 0
            x1 = []
            count1 = 0
            scraper = scraping.Director()
            scraper.builder = scraping.RRP()
            rrp = scraper.create2()
            results = rrp.temp2()
            myList = [i[1:] for i in results]
            intlist = [float(x) for x in myList]
            scraper = scraping.Director()
            scraper.builder = scraping.sale_prices()
            sale = scraper.create2()
            results = sale.temp2()
            mySaleList = [i[1:] for i in results]
            salePriceInt = [float(x) for x in mySaleList]
            while count < len(myList):
                count += 1
                x.append(count)

            while count1 < len(mySaleList):
                count1 += 1
                x1.append(count1)
            plt.figure(num=None, figsize=(10, 10), dpi=80,
                       facecolor='w', edgecolor='k')
            y = [i for i in intlist]
            y1 = [i for i in salePriceInt]
            plt.xlim(0, 22)
            plt.plot(x, y, label='RRP')
            plt.plot(x1, y1, label='Sale Price', color='r')
            plt.scatter(x, y)
            plt.scatter(x1, y1, color='r')
            plt.title('Price Comparison Chart')
            plt.ylabel('Price ($)')
            plt.xlabel('Number of products')
            for i, j in zip(y1, x1):
                plt.annotate(str(i), xy=(j, i), textcoords='data',
                             horizontalalignment='left',
                             verticalalignment='bottom')
            for i, j in zip(y, x):
                plt.annotate(str(i), xy=(j, i), textcoords='data',
                             horizontalalignment='left',
                             verticalalignment='bottom')
            plt.legend()
            plt.show()

class SavingsGraph(Graphs):
    def do_use(self):
        count = 0
        x = []
        scraper = scraping.Director()
        scraper.builder = scraping.saving_total()
        savings = scraper.create2()
        results = savings.temp2()
        myList = [i.partition('(')[-1].rpartition('%')[0] for i in results]
        str_list = filter(len, myList)
        intlist = [int(x) for x in str_list]
        while count < len(intlist):
            count += 1
            x.append(count)
        plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w',
                   edgecolor='k')
        y = [i for i in intlist]
        plt.xlim(0, 22)
        plt.ylim(0, 100)
        plt.bar(x, y)
        plt.title('Total Savings')
        plt.ylabel('Savings (%)')
        for i, j in zip(y, x):
            plt.annotate(str(i), xy=(j, i), textcoords='data',
                         horizontalalignment='left',
                         verticalalignment='bottom')
        plt.show()
