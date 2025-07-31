import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(1 + 2, 3)
        self.assertEqual(2 + 2, 4)
        self.assertEqual(-1 + 1, 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(3 - 2, 1)
        self.assertEqual(-2 - (-2), 0)
        self.assertEqual(-3 - 1, -4)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError, div, 0, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 100), 2)  #Check log with base 10 and pos#
        self.assertEqual(log(2, 8), 3)  #with base 2 and pos#
        self.assertEqual(log(math.e, math.e), 1)  #with base e, should be 1

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, log, 1, 10)  #base of 1 is invalid will raise an error
        self.assertRaises(ValueError, log, 0, 10)  #base of 0 is invalid will raise an error
    # ##########################
    
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