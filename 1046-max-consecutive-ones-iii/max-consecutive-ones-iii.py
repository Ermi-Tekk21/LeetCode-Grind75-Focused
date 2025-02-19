class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                k -= 1
            j += 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j - i