import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(first=add(a=2, b=5), second=7)
        self.assertEqual(first=add(a=-1, b=-3), second=-4)
        self.assertEqual(first=add(a=4, b=-6), second=-2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(first=sub(a=2, b=5), second=-3)
        self.assertEqual(first=sub(a=10, b=4), second=6)
        self.assertEqual(first=sub(a=7, b=8), second=-1)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(first=log(a=4, b=1), second=0)
        self.assertEqual(first=log(a=2, b=8), second=3)
        self.assertEqual(first=log(a=5, b=25), second=2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 0)

    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()