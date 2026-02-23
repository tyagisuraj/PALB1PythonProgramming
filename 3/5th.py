# Given an array arr[] of positive integers. Return true if all the array elements are
# palindrome otherwise, return false.
# Examples:
# Input: arr[] = [111, 222, 333, 444, 555]
# Output: true
# Explanation:
# arr[0] = 111, which is a palindrome number.
# arr[1] = 222, which is a palindrome number.
# arr[2] = 333, which is a palindrome number.
# arr[3] = 444, which is a palindrome number.
# arr[4] = 555, which is a palindrome number.
# As all numbers are palindrome so This will return true.
# Input: arr[] = [121, 131, 20]
# Output: false
# Explanation: 20 is not a palindrome hence the output is false

class Solution:
    def PalinArray(self, arr):
        for num in arr:
            s = str(num)
            if s != s[::-1]:
                return False
        return True
