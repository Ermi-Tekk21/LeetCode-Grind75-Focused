class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        if nums == [1]:
            return 0
        elif nums == [0]:
            return 1
        for i in range (1,size+1):
            if i not in nums:
                return (i)
            elif 0 not in nums:
                return 0