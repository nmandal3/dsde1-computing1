'''
test-tfidf_corpus.py

Test file for TFIDFCorpus class of TF-IDF exercise.
'''

import unittest
import tfidf_corpus as tf


class TestTF(unittest.TestCase):
    def set_up(self):
        pass

    def test_files(self):
        '''Test reading in the list of filenames'''
        my_tfidf = tf.TFIDFCorpus('text-files')
        result = my_tfidf.get_filenames()
        file_list = ['a-drinking-song-yeats.txt',
                     'christmas-carol.txt',
                     'mercutio.txt', 
                     'the-start-teasdale.txt']
        self.assertEqual(result, file_list)

    def test_create_docs(self):
        '''Test creation of TFDocument instances'''
        my_tfidf = tf.TFIDFCorpus('text-files')
        result = len(my_tfidf.docs)
        self.assertEqual(result, 4)
    
    def test_computeidf(self):
        '''Test generation of IDF dictionary'''
        my_tfidf = tf.TFIDFCorpus('text-files')
        k = my_tfidf.idf.keys()
        self.assertEqual(my_tfidf.idf['light'], 2.0)
        self.assertEqual(my_tfidf.idf['cold'], 4.0)
        self.assertEqual(my_tfidf.idf['time'], 2.0)
        self.assertNotIn('facebook', k)
    
    def test_gettfidf(self):
        '''Test calculation of TFIDF'''
        my_tfidf = tf.TFIDFCorpus('text-files')
        result = my_tfidf.get_tfidf('mercutio.txt', 'her')
        self.assertAlmostEqual(result, 0.008630462173553425)
        result = my_tfidf.get_tfidf('mercutio.txt', 'spider')
        self.assertAlmostEqual(result, 0.006931471805599453)
        result = my_tfidf.get_tfidf('christmas-carol.txt', 'her')
        self.assertAlmostEqual(result, 0.00040748168902518533)
        with self.assertRaises(ValueError):
            my_tfidf.get_tfidf('christmas-carol.txt', 'google')

    def test_get_top(self):
        '''Test retrieval of top terms'''
        my_tfidf = tf.TFIDFCorpus('text-files')
        result = my_tfidf.get_top_words('a-drinking-song-yeats.txt')
        self.assertEqual(result, ['comes', 'glass', 'grow', 'lift', 'sigh', "that's", 'truth', 'we', 'wine', 'mouth'])


    def test_get_three(self):
        '''Test retrieval of non-default number of terms'''
        my_tfidf = tf.TFIDFCorpus('text-files')
        result = my_tfidf.get_top_words('mercutio.txt', n=3)
        self.assertEqual(result, ['dream', "o'er", 'then'])
        
if __name__=='__main__':
    unittest.main()