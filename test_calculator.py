# https://github.com/Davidw122/lab11-dw-jc
# Partner 1: David Weisglass
# Partner 2: Javier Castro



import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(1, -2), -1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 2), -3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(-1, 2), -2)
        self.assertEqual(multiply(0, 1), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(1, 2), 2.0)
        self.assertEqual(divide(1, -2), -2.0)
        self.assertEqual(divide(2, 1), .5)

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 1)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(3, 27), 3)
        self.assertEqual(logarithm(2, 16), 4)


    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0, 8)
    ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(10, 0)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(2, 3), 13**.5)
        self.assertAlmostEqual(hypotenuse(3, 3), 18**.5)
        self.assertAlmostEqual(hypotenuse(2, 4), 20**.5)

    def test_sqrt(self): # 3 assertions

        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(3), 3 ** 0.5)
        with self.assertRaises(ValueError):
            square_root(-1)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()