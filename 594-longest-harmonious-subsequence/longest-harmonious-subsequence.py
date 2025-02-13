class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()  # Step 1: Sort the array
        left = 0  # Sliding window left pointer
        max_length = 0  # Store the max length of a harmonious subsequence

        for right in range(len(nums)):  # Expand the right pointer
            # If window becomes invalid, move left pointer
            while nums[right] - nums[left] > 1:
                left += 1  

            # Check if we have both nums[left] and nums[right] in the window
            if nums[right] - nums[left] == 1:
                max_length = max(max_length, right - left + 1)

        return max_length
