import numpy as np
arr=np.array([1,2,3],dtype='int32')
print("Data type:",arr.dtype)
arr=arr.astype('float64')
print("Data type after conversion:",arr.dtype)