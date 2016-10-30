import unittest
from Data_Method import *
from Scraping import *
from matplotlib import pyplot as plt
from matplotlib.testing.decorators import cleanup


class Scraping_Test(unittest.TestCase, Webscraping):

    def test_result_array1(self):
        """
        Testing code to check that individual array elements are not None
        """
        self.assertIsNotNone(Webscraping.temp("input", "name", "barcode", "value")[1])

    def test_result_array2(self):
        """
        Testing code two to check that individual array elements are not None
        """
        self.assertIsNotNone(Webscraping.temp2("a", "class", "blue_link fn url")[1])

    def test_array_editing(self):
        '''
        Test to see if I can edit the arrays test layout and successfully print the desired result
        '''
        results = Webscraping.temp2('div', "class", "productSearch-metainfo")  # publishingDate
        myList = [i.split(',', 1)[-1].strip() for i in results]
        self.assertNotIn('\n', myList[0])

    @cleanup
    def test_create_printpublisher(self):
        """
        Testing graph creation for publishing data to ensure graph is still created on refactoring
        """
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        fig = plt.show()
        d = DataMethods()
        d.setter(Webscraping)

        self.assertEqual(DataMethods.print_publisher(Webscraping), fig)

    @cleanup
    def test_create_pricecomparison(self):
        """
        Testing graph creation for publishing data to ensure graph is still created on refactoring
        """
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        fig = plt.show()

        self.assertEqual(DataMethods.price_comparison(self), fig)

    @cleanup
    def test_create_savingsdata(self):
        """
        Testing graph creation for publishing data to ensure graph is still created on refactoring
        """
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        fig = plt.show()
        self.assertEqual(DataMethods.total_savings_data(self), fig)

if __name__ == '__main__':
    unittest.main()
