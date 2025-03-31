"""
Complexity Analysis:
    - Time Complexity: O(logn)
    - Space Complexity: O(1)
"""

class BinarySearch:
    def find_min(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return BinarySearch().find_min(nums)