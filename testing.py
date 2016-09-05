import unittest
from Data_Method import *
from Scraping import *
from matplotlib import pyplot as plt
from matplotlib.testing.decorators import cleanup

class Scraping_Test(unittest.TestCase):

    def test_result_array(self):
        '''
        Testing code to check that individual array elements are not None
        '''
        self.assertIsNotNone(Webscraping.temp2("a", "class", "blue_link fn url", "text")[1])
        self.assertIsNotNone(Webscraping.temp("input", "name", "barcode", "value")[1])

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