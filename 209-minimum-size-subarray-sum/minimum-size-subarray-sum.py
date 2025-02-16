class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize variables for the sliding window
        left = 0
        current_sum = 0
        min_len = float('inf')  # Start with infinity for easier comparisons

        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            current_sum += nums[right]  # Expand the window by adding the right element

            # Shrink the window from the left if the current sum is >= target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)  # Update min_len
                current_sum -= nums[left]  # Shrink the window from the left
                left += 1

        # If no valid subarray is found, return 0
        return min_len if min_len != float('inf') else 0
