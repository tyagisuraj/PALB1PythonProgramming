# You are given an integer array arr[]. You need to find the maximum sum of a
# subarray (containing at least one element) in the array arr[]
class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        current_sum = arr[0]
        max_sum = arr[0]
        
        for i in range(1, len(arr)):
            # Decide whether to extend or restart
            current_sum = max(arr[i], current_sum + arr[i])
            
            # Update maximum sum found so far
            max_sum = max(max_sum, current_sum)
        
        return max_sum
