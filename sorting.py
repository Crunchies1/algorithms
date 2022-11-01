import numpy as np
import time as time

S = np.random.randn(30)
M = np.random.randn(400)
L = np.random.randn(950)

def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        # Dividing the array elements into 2 halves, finding mid point
        L, R = arr[:mid], arr[mid:] 
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def partition(array, low, high):
  
    # Choose the rightmost element as pivot
    pivot = array[high]
  
    # Pointer for greater element
    i = low - 1
  
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
  
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
  
    # Swap the pivot element with 
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
    # Return the position from where partition is done
    return i + 1
  
# Function to perform quicksort
  
  
def quickSort(array, low, high):
    if low < high:
  
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
  
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
  
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

startTime = time.time()
mergeSort(S)
mergeTime = time.time() 
quickSort(S, 0, len(S) - 1)
print(time.time() - mergeTime, mergeTime - startTime)

startTime = time.time()
mergeSort(M)
mergeTime = time.time() 
quickSort(M, 0, len(M) - 1)
print(time.time() - mergeTime, mergeTime - startTime)

startTime = time.time()
mergeSort(L)
mergeTime = time.time()
quickSort(L, 0, len(L) - 1)
print(time.time() - mergeTime, mergeTime - startTime)