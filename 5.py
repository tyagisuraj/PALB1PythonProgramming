# Given an array arr, rotate the array by one position in clockwise direction.
# Examples:
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
# Explanation: If we rotate arr by one position in clockwise 5 come to the front and
# remaining those are shifted to the end.
#User function Template for python3

class Solution:
    def rotate(self, arr):
            n = len(arr)
            
            if n == 0:
                return
            
            last = arr[n - 1]   # Step 1: Store last element
            
            # Step 2: Shift elements right
            for i in range(n - 1, 0, -1):
                arr[i] = arr[i - 1]
            
            arr[0] = last   # Step 3: Place last element at front
