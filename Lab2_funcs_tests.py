#Lab 2 Test Cases
#Name: Joshua Smith
#Section: 07
##############################################################
import unittest
import funcs
from math import pi, e
#3 test cases for each function
class TestCases(unittest.TestCase):
   def test_do_math(self):
      # Add code here.
      self.assertAlmostEqual(funcs.do_math(1, 1), 0.0909090909)
      self.assertAlmostEqual(funcs.do_math(100, -34), 0.436483425983)
      self.assertAlmostEqual(funcs.do_math(14, 37), -3.891352244560727)

   def test_quadratic_formula1(self):
      # Add code here.
      self.assertEqual(funcs.quadratic_formula1(1, 0, -36), 6)
      self.assertAlmostEqual(funcs.quadratic_formula1(14, 6, -3), 0.295816316324)
      self.assertAlmostEqual(funcs.quadratic_formula1(-5, 17, 300), -6.23032155716)

   def test_quadratic_formula2(self):
      # Add code here.
      self.assertEqual(funcs.quadratic_formula2(1, 0, -36), -6)
      self.assertAlmostEqual(funcs.quadratic_formula2(14, 6, -3), -0.724387744896)
      self.assertAlmostEqual(funcs.quadratic_formula2(-5, 17, 300), 9.63032155716)

   def test_distance(self):
      # Add code here.
      self.assertEqual(funcs.distance(12, 4, -124, 2), 138)
      self.assertEqual(funcs.distance(-5, 14, 0, 2), 17)
      self.assertEqual(funcs.distance(0, 10, -3, 94), 87)

   def test_is_positive(self):
      # Add code here.
      self.assertFalse(funcs.is_positive(-124.873426))
      self.assertTrue(funcs.is_positive(0))
      self.assertTrue(funcs.is_positive(pi * e))

   def test_dividable_by_7(self):
      # Add code here.
      self.assertTrue(funcs.dividable_by_7(-49))
      self.assertTrue(funcs.dividable_by_7(0))
      self.assertFalse(funcs.dividable_by_7(9))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

