import unittest
from practice import Client
from mock import patch, Mock

class TestPractice(unittest.TestCase):
    @unittest.skip("TODO")
    def test_successful_purchase(self):
        '''
        Client can make a purchase if their account balance is at least equal to the product price
        '''
        pass
        
    @unittest.skip("TODO")
    def test_failed_purchase(self):
        '''
        Client cannot make a purchase if their account balance is lower than the product price
        '''
        pass
        
if __name__ == '__main__':
    unittest.main()