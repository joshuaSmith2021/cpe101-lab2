#Lab 2 Functions
#Name: Joshua Smith
#Section: 07
import math

#1)purpose statement:This function compute a given formula
# signature:int int -> float
def do_math (x, y):
   return (x**2 - (3 / 5) * x * y**2) / (2 * x**2 * y / 5 + 4)

#2)purpose statement:This function computes the quadratic formula
#                    The quadratic formula returns two values;
#                    this function returns one of them.
# signature:int int int -> float
def quadratic_formula1 (a, b, c):
   return (-1 * b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)

#3)purpose statement:This function computes the quadratic formula
#                    The quadratic formula returns two values;
#                    this function returns one of them.
# signature:int int int -> float
def quadratic_formula2 (a, b, c):
   return (-1 * b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

#4)purpose statement:This function computes the Manhattan distance
#                    between two points
# signature:int int int int -> int
def distance (x1, y1, x2, y2):
   return abs(x1 - x2) + abs(y1 - y2)

#5)purpose statement:Determine if given float is positive
# signature:float -> bool
def is_positive (num):
   return num >= 0

#6)purpose statement:Determine if given integer is divisible by 7
# signature:int -> bool
def dividable_by_7 (num):
   return num % 7 == 0

