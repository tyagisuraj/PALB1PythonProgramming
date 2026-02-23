# You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the
# array is sorted in non-decreasing order. Your task is to find and return the index of the
# first row that contains the maximum number of 1s. If no such row exists, return -1.
# Note:
# • The array follows 0-based indexing.
# • The number of rows and columns in the array are denoted
# by n and m respectively
class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        
        max_row_index = -1
        j = m - 1   # Start from top-right corner
        
        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                j -= 1
                max_row_index = i
        
        return max_row_index
