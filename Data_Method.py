from scraping import *
import re
from matplotlib import pyplot as plt


class Data_Methods(Webscraping):

    def products_table(webscraping):
            fig, axs = plt.subplots(2, 1)
            clust_data = (webscraping.product_name(),
                          webscraping.isbn(),
                          webscraping.publishing_data(),
                          webscraping.RRP(),
                          webscraping.sale_prices(),
                          webscraping.saving_total(),
                          webscraping.photo_link())
            collabel = ("Product Name", "ISBN", "Publishing Date", "RRP (NZ$)",
                        "Sale Price (NZ$)", "Savings (%)")
            axs[0].axis('tight')
            axs[0].axis('off')
            the_table = axs[0].table(cellText=clust_data,
                                     colLabels=collabel, loc='center')
            plt.show()

    def price_comparison(webScraping):
            x = []
            count = 0
            x1 = []
            count1 = 0
            intlist = [float(x) for x in webScraping.RRP()]
            salePriceInt = [float(x) for x in webScraping.sale_prices()]
            while count < len(webScraping.RRP()):
                count += 1
                x.append(count)

            while count1 < len(webScraping.sale_prices()):
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
            plt.scatter(x1, y1,  color='r')
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

    def total_savings_data(webScraping):
            count = 0
            x = []
            str_list = filter(len, webScraping.saving_total())
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

    def publishing_data(webScraping):
            January = []
            February = []
            March = []
            April = []
            May = []
            June = []
            July = []
            August = []
            September = []
            October = []
            November = []
            December = []

            result = re.findall(r"(?i)\b[a-z]+\b", str
                                (webScraping.publishing_date()))
            for strings in result:
                if strings == "January":
                            January.append(1)
                elif strings == "February":
                            February.append(1)
                elif strings == "March":
                            March.append(1)
                elif strings == "April":
                            April.append(1)
                elif strings == "May":
                            May.append(1)
                elif strings == "June":
                            June.append(1)
                elif strings == "July":
                            July.append(1)
                elif strings == "August":
                            August.append(1)
                elif strings == "September":
                            September.append(1)
                elif strings == "October":
                            October.append(1)
                elif strings == "November":
                            November.append(1)
                elif strings == "December":
                            December.append(1)

                # Data to plot
            labels = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October',
                      'November', 'December']
            sizes = [len(January), len(February), len(March), len(April),
                     len(May), len(June), len(July),
                     len(August), len(September), len(October),
                     len(November), len(December)]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue',
                      'red', 'black', 'blue', 'yellow', 'green',
                      'purple', 'orange', 'darkblue']
            explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)

            plt.axis('equal')
            plt.show()
