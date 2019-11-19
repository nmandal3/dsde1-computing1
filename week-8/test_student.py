'''
test_student.py

Test file for DesEngStudent class.
'''


import unittest
import student as student


class TestStudent(unittest.TestCase):
    def set_up(self):
        pass

    def test_print(self):
        '''
        Test returning a string for easy printing
        '''
        my_student = student.DesEngStudent('Becky Stewart', 2, 20)
        result = my_student.print()
        self.assertEqual(result, 'Becky Stewart (DE2) with £20 remaining')

    def test_paper(self):
        '''
        Test paper print spend
        '''
        my_student = student.DesEngStudent('Becky Stewart', 2, 20)
        result = my_student.paper_print(3)
        self.assertEqual(result, 19.7)
    
    def test_threed_d(self):
        '''
        Test 3D print spend
        '''
        my_student = student.DesEngStudent('Becky Stewart', 2, 20)
        result = my_student.three_d(2)
        self.assertEqual(result, 9)
    
    def test_laser(self):
        '''
        Test 3D print spend
        '''
        my_student = student.DesEngStudent('Becky Stewart', 2, 20)
        result = my_student.laser_cut(4)
        self.assertEqual(result, 16)
    
    def test_spend_error(self):
        '''
        Test overspending raises error
        '''
        my_student = student.DesEngStudent('Becky Stewart', 2, 20)
        with self.assertRaises(ValueError):
            result = my_student.spend(22)

if __name__ == '__main__':
    unittest.main()
