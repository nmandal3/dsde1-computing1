# Week 9 Thursday Exercises - Inheritance and More Files

## Simple Classes with Inheritance
1. Implement a class called `ImperialStudent` with instance attributes that you can set at instantiation (`my_student = ImperialStudent('Alice Gast', '12345678')`):

* name
* cid

2. Implement a second class that extends `ImperialStudent`. Call it `DEStudent` and give it the addional instance attributes:

* year
* tutor

3. Give the `DEStudent` a class attribute of

* faculty

3. Add a method to the `ImperialStudent` class that returns whether a student can check out a book from the library.

4. Add a method only to the `DEStudent` class that returns whether a student has passed the ACE Workshop induction.

5. Verify in the Python shell that an instance of a `DEStudent` class can access book the library and workshop methods, but that an `ImperialStudent` can't access the workshop method.

6. Print out the attributes for each type of class and verify that the instance attributes and class attributes are associated where you expect them.



## Manipulating Image Files

1. Check if scikit-image is already installed on your machine. In a Python interactive shell type:

```
import skimage
```

    If no errors are printed, it's already installed and you can skip the next step.

2. If you need to install the package, then you can use `pip` or `conda` (best to use whichever you have used so far in this module). You can follow [the instructions on the scikit-image site](https://scikit-image.org/docs/stable/install.html).

3. Use the file `manipulating-images.py` as a start to display a photo.

4. Modify the file so that you display a black and white version of the photo instead of full colour.

5. Now tint the black and white version pink.


## Manipulating CSV Files
1. Using the `genfromtxt()` from numpy, read in the data in the csv file in the exercise repo.

2. Read through the [documentation about the data](https://www.kaggle.com/hmavrodiev/london-bike-sharing-dataset/data) in the csv file to understand how it is arrange. 

3. Calculate the average temperature across the whole data set.

4. Calculate the daily average temperature (one data point per day).

5. Plot the a bar chart of the number of hire counts made over time.
