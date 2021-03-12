from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

example_file = glob.glob(r'/home/jonesy/Desktop/BelajarPyton/wint_sky.gif')[0]
im = imread(example_file)
plt.imshow(im)	
plt.show()

