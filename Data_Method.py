from Scraping import *
import re
from matplotlib import pyplot as plt


class DataMethods(Webscraping):
    def setter(self, webscraping):
        months = ['January', 'February', 'March', 'April', 'May',
                  'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

        global month_list
        result = re.findall(r"(?i)\b[a-z]+\b", str
                            (webscraping.publishing_date(self)))

        month_list = [[], [], [], [], [], [], [], [], [], [], [], []]

        x = 0
        while x <= 11:
            for strings in result:
                if strings == months[x]:
                    month_list[x].append(1)
            x += 1

    def print_publisher(self):
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

    def price_comparison(webscraping):
        x = []
        count = 0
        x1 = []
        count1 = 0
        intlist = [float(x) for x in webscraping.RRP()]
        salePriceInt = [float(x) for x in webscraping.sale_prices()]
        while count < len(webscraping.RRP()):
            count += 1
            x.append(count)

        while count1 < len(webscraping.sale_prices()):
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

    def total_savings_data(webscraping):
        count = 0
        x = []
        str_list = filter(len, webscraping.saving_total())
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
