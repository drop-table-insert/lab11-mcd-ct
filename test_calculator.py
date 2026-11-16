import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(first=add(a=2, b=5), second=7)
        self.assertEqual(first=add(a=-1, b=-3), second=-4)
        self.assertEqual(first=add(a=4, b=-6), second=-2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(first=subtract(a=2, b=5), second=-3)
        self.assertEqual(first=subtract(a=10, b=4), second=6)
        self.assertEqual(first=subtract(a=7, b=8), second=-1)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,2),4)
        self.assertEqual(mul(5,10),50)
        self.assertEqual(mul(1,3),3)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,12),4)
        self.assertEqual(div(2,6),3)
        self.assertEqual(div(3,1),1/3)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(first=logarithm(a=4, b=1), second=0)
        self.assertEqual(first=logarithm(a=2, b=8), second=3)
        self.assertEqual(first=logarithm(a=5, b=25), second=2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 0)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
           logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
         self.assertEqual(hypotenuse(5,12),13)
         self.assertEqual(hypotenuse(3,4),5)
         self.assertEqual(hypotenuse(-5,-12),13)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(25),5)
        self.assertEqual(square_root(100),10)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()