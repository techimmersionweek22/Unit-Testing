import unittest
from practice import Client
from mock import patch, Mock

class TestPractice(unittest.TestCase):
    def test_successful_purchase(self):
        mock_product = Mock()
        mock_product.name = "Laptop"
        mock_product.price = 1200
        client = Client("Alice", 2000)
        client.purchase(mock_product)
        self.assertEqual(client.account_balance, 800)
        self.assertEqual(client.purchases, ["Laptop"])
        
    def test_failed_purchase(self):
        mock_product = Mock()
        mock_product.name = "Laptop"
        mock_product.price = 1200
        client = Client("Alice", 200)
        client.purchase(mock_product)
        self.assertEqual(client.account_balance, 200)
        self.assertEqual(client.purchases, [])
        
if __name__ == '__main__':
    unittest.main()