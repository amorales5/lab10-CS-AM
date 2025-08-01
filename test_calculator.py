#https://github.com/amorales5/lab10-CS-AM.git
#Partner 1: Crystal Schmitt
#Partner 2: Alexsis Morales

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual((add(2,2)), 4)
        self.assertEqual(add(-1,1), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3,2), 1)
        self.assertEqual(subtract(2,2), 0)
        self.assertEqual(subtract(-3,1), -4)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,2), 10)
        self.assertEqual(mul(0,10), 0)
        self.assertEqual(mul(100, -1), -100)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(-5,10), -2)
        self.assertEqual(div(1,10), 10)
        self.assertEqual(div(2,64), 32)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError, div, 0, 5)  #Dividing by zero will raise an error

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 100), 2)  #Check log with base 10 and pos#
        self.assertEqual(logarithm(2, 8), 3)  #with base 2 and pos#
        self.assertEqual(logarithm(math.e, math.e), 1)  #with base e, should be 1

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, logarithm, 1, 10)  #base of 1 is invalid will raise an error
        self.assertRaises(ValueError, logarithm, 0, 10)  #base of 0 is invalid will raise an error
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
             logarithm(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(6,8), 10)
        self.assertEqual(hypotenuse(30,40), 50)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()