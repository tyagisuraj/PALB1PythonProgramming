# Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and
# columns is always odd. Return the median of the matrix.
import bisect

class Solution:
    def median(self, matrix):
        
        n = len(matrix)
        m = len(matrix[0])
        
        # Step 1: Find min and max
        low = min(row[0] for row in matrix)
        high = max(row[m-1] for row in matrix)
        
        desired = (n * m) // 2
        
        while low < high:
            mid = (low + high) // 2
            
            count = 0
            for row in matrix:
                count += bisect.bisect_right(row, mid)
            
            if count <= desired:
                low = mid + 1
            else:
                high = mid
        
        return low
