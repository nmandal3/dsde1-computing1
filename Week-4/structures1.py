'''
structures.py
Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    first = the_list[0]
    last = the_list[-1]
    both = [first, last]
    return both


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception.
def part_reverse(the_list, beginning, end):
    try :
        semilist = the_list[beginning:end]
        semilist.reverse()
    except ValueError :
        return False 
    return semilist # hint this is incomplete


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    semilist = the_list[0:index]
    a = the_list[index]
    for i in range(0, index) :
        semilist.append(a)
    newlist = semilist + the_list[(index+1):]
    return newlist


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    a = word.lower()
    b = word[::-1].lower()
    if a == b:
        return True
    else :
        return False

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    a = ''
    for i in sentence:
        if i.isalpha():
            a += i.lower()
    b = a[::-1].lower()
    print (a + '   ' + b)
    print ('')
    if a == b:
        return True
    else :
        return False

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end. The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    s3 = ''
    punctuation = ['.', '?', '!']
    if sentence1[0] == '':
        sentence1 = sentence1[1:]
    if sentence2[0] == '':
        sentence2 = sentence2[1:]
    if sentence1[-1] == '':
        sentence1 = sentence1[0:-1]
    if sentence2[-1] == '':
        sentence2 = sentence2[0:-1]
    s3 = sentence1 + ' ' + sentence2 
    if sentence1[0].isupper() and sentence2[0].isupper():
        if sentence1[-1] in punctuation and sentence2[-1] in punctuation:
            return s3
    print (s3)
    return


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    d3 = dictionary1.update(dictionary2)
    return d3