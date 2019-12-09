'''
tfidf_corpus_solution.py

Solution file for a TFIDFCorpus class for the TF-IDF exercise.
'''

import math
import os
import tf_document as tf

class TFIDFCorpus:
    def __init__(self, folder):
        '''Given a folder location, create a TFDocument for each
        .txt file within the folder and populate an instance attribute
        called idf.'''

        # save location in attribute
        # get a list of all txt files in the folder
        # create a TFDocument for each txt file
        # create a dictionary with the (not yet normalised, log not taken) 
        # IDF value for each term that occurs in the corpus

        return

    def get_filenames(self):
        '''Returns a list of filenames whose extension is txt within
        a the corpus's folder.'''

        return
    
    def create_documents(self, filenames):
        '''Create a dict of keys with the listed filenames relative 
        to the corpus folder and values of the TFDocument instance.'''
        # create empty dictionary
        # instantiate a new TFDocument for each file in the dictionary

        return
    
    def compute_idf(self):
        '''Populate a dictionary stored in the instance attribute idf
        with:
         - keys of terms that occur across the whole corpus
         - values of total num of docs / num of docs where term occurs'''

        # for each TFDocument
        # and for each key in the document
        # add any additional terms not seen before other docs
        # increment the counts of terms seen before in other docs
        
        # for each value, replace with total num of docs / count

        return

    def get_tfidf(self, filename, word):
        '''Return the TDIDF value of the given word in the given filename 
        (not including the folder in the filename).
        
        If the word is not in the corpus, it raises a ValueError.'''

        # retrieve TF for word
        # if not in document, set to 0
        
        # checking first if the word exists in the corpus
        # TFIDF = TF x log_e(IDF)
        # if word not in the corpus raise a ValueError
        
        return


    def get_top_words(self, filename, n=10):
        '''Return the N words with the highest TFIDF values in the given
        file.'''
        # get the list of words for the document
        
        # generate the TFIDF values for all words in the file
                
        # sort the list

        return 