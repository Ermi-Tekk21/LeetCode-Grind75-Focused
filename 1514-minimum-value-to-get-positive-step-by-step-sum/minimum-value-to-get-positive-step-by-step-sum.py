class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
            
        for i in range (1, len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i-1])
            
        min_num = min(prefix_sum) 
        target = 1-min_num
        if target > 0:
            return target
        else:
            return 1