import unittest
from practice import Client
from unittest.mock import Mock

class TestPractice(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.mock_product = Mock()
        self.mock_product.name = "Laptop"
        self.mock_product.price = 1200
    
    def test_successful_purchase(self):
        client = Client("Alice", 2000)
        client.purchase(self.mock_product)
        self.assertEqual(client.account_balance, 800)
        self.assertEqual(client.purchases, ["Laptop"])
        
    def test_failed_purchase(self):
        client = Client("Alice", 200)
        client.purchase(self.mock_product)
        self.assertEqual(client.account_balance, 200)
        self.assertEqual(client.purchases, [])
        
if __name__ == '__main__':
    unittest.main()