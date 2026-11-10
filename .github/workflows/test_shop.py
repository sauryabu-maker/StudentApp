import unittest
from shop import calculate_total

class TestShop(unittest.TestCase):
    def test_total(self):
        self.assertEqual(calculate_total(100, 3), 300)

if __name__ == "__main__":
    unittest.main()
