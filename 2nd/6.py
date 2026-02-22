# Given an integer n, find its factorial. Return a list of integers denoting the digits
# that make up the factorial of n.
# Examples:
# Input: n = 5
# Output: [1, 2, 0]
# Explanation: 5! = 1*2*3*4*5 = 120
# Input: n = 10
# Output: [3, 6, 2, 8, 8, 0, 0]
# Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
# Input: n = 1
# Output: [1]
# Explanation: 1! = 1
class Solution:
    def factorial(self, n):
        # Store digits in reverse order
        result = [1]
        
        for num in range(2, n + 1):
            carry = 0
            
            for i in range(len(result)):
                product = result[i] * num + carry
                result[i] = product % 10
                carry = product // 10
            
            # Add remaining carry
            while carry:
                result.append(carry % 10)
                carry //= 10
        
        # Reverse to get correct order
        return result[::-1]
