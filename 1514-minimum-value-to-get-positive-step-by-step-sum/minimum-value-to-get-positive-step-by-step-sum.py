class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
    
        for i in range (1, len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i-1])
            
        target = 1-min(prefix_sum) 
        
        return target if target > 0 else 1