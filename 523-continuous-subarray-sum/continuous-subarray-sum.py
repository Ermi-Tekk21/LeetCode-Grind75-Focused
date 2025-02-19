class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_remainders = {0: -1}  # Dictionary to store remainders and their first occurrence index
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k  # Compute remainder
            
            if remainder in prefix_remainders:
                if i - prefix_remainders[remainder] > 1:  # Ensure subarray size is at least 2
                    return True
            else:
                prefix_remainders[remainder] = i  # Store first occurrence of remainder
        
        return False
