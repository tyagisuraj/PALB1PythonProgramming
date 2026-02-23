# You are given a rectangular matrix mat[][] of size n x m, and your task is to return an
# array while traversing the matrix in spiral form.
# Examples:
# Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
# Explanation:
# Input: mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
# Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
# Explanation: Applying same technique as shown above.
# Input: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
# Output: [32, 44, 27, 23, 62, 50, 28, 54]
# Explanation: Applying same technique as shown above, output will be [32, 44, 27, 23,
# 62, 50, 28, 54].
class Solution:
    def spiralOrder(self, mat):
        result = []
        
        if not mat:
            return result
        
        n = len(mat)
        m = len(mat[0])
        
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        
        while top <= bottom and left <= right:
            
            # 1. Left → Right
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            
            # 2. Top → Bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # 3. Right → Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            
            # 4. Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        
        return result
