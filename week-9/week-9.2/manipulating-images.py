'''
Manipulating images

Using skimage and numpy to do image processing.

'''

import numpy as np
from skimage import data, io
import matplotlib.pyplot as plt


picture = io.imread('./images/tower.jpg')

plt.figure(figsize=(4, 4))
plt.imshow(picture, cmap='gray')
plt.axis('off')
plt.show()