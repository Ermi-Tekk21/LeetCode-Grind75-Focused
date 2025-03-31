class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1

        while start < end:
            current_sum = nums[start] + nums[end]
            if current_sum == target:
                return [start + 1, end + 1] 
            elif current_sum > target:
                end -= 1  
            else:
                start += 1 

        return [-1, -1] 