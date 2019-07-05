import unittest
from models import Quotes
Quotes = quotes.Quotes

class QuotesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quotes class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quotes = Quotes("Larry DeLuca","id":37,"quote":"I\u2019ve noticed lately that the paranoid fear of computers becoming intelligent and taking over the world has almost entirely disappeared from the common culture.  Near as I can tell, this coincides with the release of MS-DOS.","permalink":"http://quotes.stormconsultancy.co.uk/quotes/37")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quotes,Quotes))


if __name__ == '__main__':
    unittest.main()