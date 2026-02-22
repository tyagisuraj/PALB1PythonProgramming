# Given three sorted arrays in non-decreasing order, print all common elements
# in non-decreasing order across these arrays. If there are no such elements return
# an empty array. In this case, the output will be -1.
# Note: can you handle the duplicates without using any additional Data Structure?
def commonElements(arr1, arr2, arr3):
    i = j = k = 0
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    
    result = []
    
    while i < n1 and j < n2 and k < n3:
        
        # If all elements are equal
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            
            x = arr1[i]
            
            # Skip duplicates in arr1
            while i < n1 and arr1[i] == x:
                i += 1
            
            # Skip duplicates in arr2
            while j < n2 and arr2[j] == x:
                j += 1
            
            # Skip duplicates in arr3
            while k < n3 and arr3[k] == x:
                k += 1
        
        # Move pointer of smallest element
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    
    return result if result else [-1]
