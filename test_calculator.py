import unittest
from calculator import add, subtract ,product ,division


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5),15)
     
    def test_subtract(self):
        self.assertEqual(subtract(10, 5),5)
    
    def test_product(self):
       self.assertEqual(product(3, 2),6)
    
    def test_division(self):
        self.assertEqual(division(10, 2),0)

if __name__=="__main__":
    unittest.main()