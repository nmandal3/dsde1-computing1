'''
exploring_numpy.py

Getting comfortable with creating and manipulating
numpy arrays.
'''

import numpy as n
import math as m

# return an array 8 items that can be any number 
# i.e. doesn't matter what you fill it with, it's
# the size that is important

def create_array8():
    a = n.array([0, 1, 2, 3, 4, 5, 6, 7])
    return a

# return a 4 x 6 array filled with any number 
# i.e. doesn't matter what you fill it with, it's
# the size that is important
def create_array6_4():
    a = n.array([
        [0, 1, 2, 3,],
        [10, 11, 12, 13],
        [20, 21, 22, 23],
        [30, 31, 32, 33],
        [40, 41, 42, 43],
        [50, 51, 52, 53]])
    return a

# return a 2x3 array of zeros w
# hint: you don't need to call array
def create_zeros2_3():
    a = n.zeros([2, 3])
    return a


# return a one-dimensional array that starts
# at 3 and counts up to 96
# 3, 4, 5 ... 94, 95, 96
def create96():
    a = n.arange(3, 97)
    return a


# create a function that takes in the following:
#   - starting number
#   - number of rows
#   - number of columns
# return an array that starts at the starting number 
# and counts up ending at 
# starting number + rows x columns
# with the input number of rows and columns
# for example, starting at 3 and 3 rows with 4 columns:
#  [3, 4, 5, 6]
#  [7, 8, 9, 10]
#  [11, 12, 13, 14]
def algo_array1(start, row, col):
    a = start + row * col
    b = n.arange(start, a).reshape(row, col)
    return b

# create a function that will return an array 
# that contains a number of values passed in
# as an input argument evenly spaced from 0 to 2*pi
# hint: you can generate it algorithmically
# with a numpy function
def algo_array2(i):
    p = m.pi
    a = n.linspace(0, 2*p, i)
    return a

# create a function with one input argument
# which takes an input value of a postive number
# it returns a dictionary with the following
#  key/value pairs:
#  'odd': array of odd numbers from 1 to input argument (inclusive)
#  'even': array of even numbers from 2 to input argument (inclusive)
# hint: you don't need a for loop
def odd_even(i):
    a = {'odd': (n.arange(1, i+1, 2)), 'even': (n.arange(2, i+1, 2))}
    return a