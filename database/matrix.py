import os
import numpy as np 

d = "/home/jonesy/projects/BelajarPyton/database/"
#float_formatter = "{:.2f}".format // gak berhasil

for filx in os.listdir(d):
	if not filx.endswith(".mnn"):
		continue
	else:
		filex=d+filx

f = open(filex)
numpy_array = np.loadtxt(f, delimiter=",")


b=numpy_array[:,-1] #extract last column
a=numpy_array[:,0:-1] #exract all colum except last column
a=np.linalg.inv(a)    

hasil=np.matmul(a,b)

np.set_printoptions(precision=2)
print(hasil)