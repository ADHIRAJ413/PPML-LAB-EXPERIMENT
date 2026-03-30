import numpy as np
a = np.array([1, 2, 3])
print(a)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)    
n = int(input("Enter N: "))
arr = np.arange(1, n+1) 
print("Array from 1 to", n, ":", arr)
sum_arr = np.sum(arr)
print("Sum of array elements:", sum_arr)    
mean_arr = np.mean(arr)
print("Mean of array elements:", mean_arr)  
max_arr = np.max(arr)
print("Maximum element in the array:", max_arr) 
min_arr = np.min(arr)
print("Minimum element in the array:", min_arr)
even_arr = arr[arr % 2 == 0]
print("Even numbers in the array:", even_arr)
odd_arr = arr[arr % 2 != 0]
print("Odd numbers in the array:", odd_arr)
greater_than_mean = arr[arr > mean_arr]
print("Elements greater than the mean:", greater_than_mean) 
less_than_mean = arr[arr < mean_arr]
print("Elements less than the mean:", less_than_mean)   
half_arr = arr / 2  
print("Array elements divided by 2:", half_arr)
    
