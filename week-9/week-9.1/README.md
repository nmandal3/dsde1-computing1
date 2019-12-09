# Week 9 Tuesday Exercises - More Practice with Classes

## Building on the Resistor Class

1. Return to the Resistor Class you wrote in Week 8-1. You probably was to copy the file into this folder and edit it separately from the version you wrote last week. Move the the resistor colour code dictionary from being a local variable inside a function to being a class attribute. Do the same with the dictionary of the tolerance colours - remove it from the min and max methods and make it a class attribute. Update the methods that use those dictionaries. You can test if it works correctly by printing the attribute directly:

'''
import resistor as r
print( r.Resistor.resist_colours )
print ( r.Resistor.tol_colours )
'''

2. Overload the built-in `__add__()` so  you can run the below code and have it return the value of the two resistors values added in series (the sum of their resistance values).

```
>>> import resistor as r
>>> my_r1 = r.Resistor('yellow', 'violet', 'brown', 'gold')
>>> my_r2 = r.Resistor('orange', 'violet', 'brown', 'gold')
>>> my_r1 + my_r2
840
```

## Continuing the TFIDF Exercise

1. Open the Python file `tf_document.py` located in the same directory as this README. Complete the methods which have been started for you. Some suggestions about what the algorithm could be are included in comments. Note that you can largely copy the code from the Week 8-2 exercise, but there are some minor changes in how this class is structured, so read carefully.

2. Use the test file `test_tf_document.py` to evaluate your code.

3. Open the Python file `tfidf_corpus.py` and complete the methods.

4. Use the test file `test_tfidf_corpus.py` to evaluate your code.

5. You can now query the corpus, for instance asking for the top 5 words for `mercutio.txt`.

```
>>> import tfidf_corpusn as ti
>>> my_ti = ti.TFIDFCorpus('./text-files')
>>> my_ti.get_top_words('mercutio.txt')
>>> my_ti.get_top_words('mercutio.txt', n=3)
['dream', "o'er", 'then']
```

6. Draw the class diagram for the two classes you've implemented.

