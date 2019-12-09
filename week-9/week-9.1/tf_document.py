'''
tf_document_solution.py

Solution file for TFDocument class of the TF-IDF exercise.
'''

import string
import math

class TFDocument:
    def __init__(self, location):
        '''Given a text file location, populates the instance
        attribute tf with the Term Frequency of that file.'''

        # save location in attribute
        # parse string and populate the tf attribute

        return

    def read_file(self):
        '''Opens a text file at the given location and returns 
        a string of its contents.'''

        return 
    
    def string_to_list(self, input_string):
        '''Takes in a string and returns a list of strings with all
        whitespace removed along with any edge punctuation. Inner 
        punctuation such as "that's" will remain.'''
        # ensure everything is lowercase
        # split into words at whitespace
        # remove any non-alpha characters at the beginning 
        # or end of each word

        return 

    def compute_tf(self, words):
        '''Given a list of strings, return a dictionary where each key is
        a string and the corresponding value is the Term Frequency for that
        string normalised to number of unique strings in the original list.'''
        # remove any repeated words
        # calculate total number of words

        return

    def get_tfidf(self, word, idf):
        '''Given a word and its IDF value, return the TFIDF value for 
        that word.'''
        return 
