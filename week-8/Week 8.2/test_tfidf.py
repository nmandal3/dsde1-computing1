'''
test-tfidf.py

Test file for TF-IDF exercise.
'''

import unittest
import tfidf as t


class TestTfidf(unittest.TestCase):
    def set_up(self):
        pass

    def test_read(self):
        '''Test reading in a file as a string'''
        my_t = t.TfIdf()
        result = my_t.read_file('./text-files/a-drinking-song-yeats.txt')
        self.assertEqual(result, 'Wine comes in at the mouth\nAnd love comes in at the eye;\nThat\'s all we shall know for truth\nBefore we grow old and die.\nI lift the glass to my mouth,\nI look at you, and I sigh.')
    
    def test_string_short(self):
        '''
        Test breaking up a string
        '''
        my_t = t.TfIdf()
        test_string = '''How now brown Cow?
        Peter piper.'''
        result = my_t.string_to_list(test_string)
        self.assertEqual(result, ['how', 'now', 'brown', 'cow', 'peter', 'piper'])

    def test_line_breaks(self):
        '''Test string with line breaks'''
        my_t = t.TfIdf()
        test_string = "Wine comes in at the mouth\nAnd love comes in at the eye;\nThat\'s all we shall know for truth\nBefore"
        result = my_t.string_to_list(test_string)
        self.assertEqual(result, ['wine', 'comes', 'in', 'at', 'the', 'mouth', 'and', 'love', 'comes', 'in', 'at', 'the', 'eye', "that's", 'all', 'we', 'shall', 'know', 'for', 'truth', 'before'])
    
    # def test_tf(self):
    #     '''
    #     Test computing TF
    #     '''
    #     my_t = t.TfIdf()
    #     test_list = ['how', 'now', 'the', 'brown', 'cow', 'peter', 'piper', 'cow', 'the', 'the', 'picked','peppers','peck']
    #     result = my_t.compute_tf(test_list)
    #     self.assertEqual(result, {'how':0.1, 
    #                               'now':0.1,
    #                               'the':0.3,
    #                               'brown':0.1,
    #                               'cow':0.2,
    #                               'peter':0.1,
    #                               'piper':0.1,
    #                               'picked':0.1,
    #                               'peck':0.1,
    #                               'peppers':0.1 })
    

if __name__=='__main__':
    unittest.main()