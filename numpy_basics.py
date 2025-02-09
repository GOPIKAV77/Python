
# Numpy is library in python used to perform high level of mathematical functions on arrays.

import numpy as np
import matplotlib.pyplot as plt
# creating a 1D array 
exp1 = np.array([1,2,3]) 

print(exp1)

#Adding arrays

exp2 = np.array([1,4,5])
print(exp1+exp2)

# Mutiplipying arrays

print(exp1*exp2)

#creating a 2D array
exp3 = np.array([[1,2],[1,4]])
print(exp3)

#print(exp2+exp3)
#Note a 2D array and 1D array cannot be added

exp4 = np.array([[3,4],[5,5]])
print(exp3/exp4) # dividing arrays 

print(exp3-exp4)


#changing a 3D array to 2D array

exp5 = np.array([[[1,2],[3,4]],[[4,5],[6,7]]])
print(exp5)

# The 3D array is of the shape (2,2,2) - the first element means 2D array that means,[[1,2],[3,4]] and[[4,5],[6,7]] . The 
# The second 2 means 2 rows and last 2 denoted 2-columns.So in total 2*2*2 = 8

# converting to a 2D array

exp6 = exp5.reshape(-1,exp5.shape[-1])
print(exp6)

#exp6 will be of the shape(4,2) ,exp5.shape[-1]=2 is the last element of (2,2,2)
# 2*2*2 = 8 .now , x*2 = 8 .i.e, x= 4 

# absolute value of array

exp7 = np.array([1,-2,6,-7])
print(np.abs(exp7)) # change - value inside arary to positive

# plotting for arary

plt.plot(np.array([1,2,3]),np.array([8,4,8]))

#output

[1 2 3]
[2 6 8]
[ 1  8 15]
[[1 2]
 [1 4]]
[[0.33333333 0.5       ]
 [0.2        0.8       ]]
[[-2 -2]
 [-4 -1]]
[[[1 2]
  [3 4]]

 [[4 5]
  [6 7]]]
[[1 2]
 [3 4]
 [4 5]
 [6 7]]
[1 2 6 7]


