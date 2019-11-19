'''
test_exploring_numpy.py

Test file for numpy basics.
'''

'''
test_toys.py

Unit tests for toy functions.
'''


import unittest
import numpy as np
import numpy.testing as npt
import exploring_numpy as ex


class TestNumpy(unittest.TestCase):
    def test_array8(self):
        '''
        Test size of 8x1 array
        '''
        result = ex.create_array8().shape
        self.assertEqual(result, (8,))

    def test_array64(self):
        '''
        Test size of 6x4 array
        '''
        result = ex.create_array6_4().shape
        self.assertEqual(result, (6,4))
    
    def test_zeros_size(self):
        '''
        Test size of 2x3 array of zeros
        '''
        result = ex.create_zeros2_3().shape
        self.assertEqual(result, (2,3))
    
    def test_zeros_content(self):
        '''
        Test content of 2x3 array of zeros
        '''
        result = ex.create_zeros2_3()
        npt.assert_equal(result, np.array([[0, 0, 0], [0, 0, 0]]))

    def test_up_to_96(self):
        '''
        Test array starting at 3 counting up to 96
        '''
        result = ex.create96()
        npt.assert_equal(result, np.arange(94) + 3)
    
    def test_algo1(self):
        '''
        Test algorithmically generated array
        '''
        result = ex.algo_array1(3, 3, 4)
        correct_answer = np.array([[3, 4, 5, 6],
                                   [7, 8, 9, 10],
                                   [11, 12, 13, 14]])
        npt.assert_equal(result, correct_answer)
    
    def test_algo2(self):
        '''
        Test second algorithmically generated array
        '''
        result = ex.algo_array2(5)
        correct_answer = np.array([ 0., 1.57079633, 3.14159265, 4.71238898, 6.28318531])
        npt.assert_allclose(result, correct_answer)
    
    def test_even(self):
        '''
        Test dict of odd and even numbers with even max value
        '''
        result = ex.odd_even(8)
        correct_answer = {'odd':np.array([1., 3., 5., 7.]),
                          'even':np.array([2., 4., 6., 8.])}
        npt.assert_equal(result, correct_answer)

    def test_odd(self):
        '''
        Test dict of odd and even numbers with odd max value
        '''
        result = ex.odd_even(9)
        correct_answer = {'odd':np.array([1., 3., 5., 7., 9.]),
                          'even':np.array([2., 4., 6., 8.])}
        npt.assert_equal(result, correct_answer)

    


if __name__ == '__main__':
    unittest.main()
