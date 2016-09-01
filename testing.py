import unittest
from Data_Method import *
from matplotlib import pyplot as plt
from matplotlib.testing.decorators import cleanup

class Scraping_Test(unittest.TestCase):

    def test_name(self):
        '''
        Testing code of string formatter for validity, hardcoded as url is usually set through CMD before running
        '''
        self.assertTrue(Webscraping.product_name(self) != [])

@cleanup
class Data_Test(unittest.TestCase):
    '''
    Testing graph creation for publishing data to ensure graph is still created on refactoring
    '''
    def test_create_figure(self):
        fig = plt.figure()

        self.assertEqual(Data_Methods.publishing_data() == fig)


if __name__ == '__main__':
    unittest.main()