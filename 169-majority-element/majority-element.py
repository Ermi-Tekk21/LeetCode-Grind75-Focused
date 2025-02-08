class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        modNums = set(nums)
        modNumdict = {}

        for i in modNums:
            modNumdict[i] = nums.count(i)

        maxValue = max(modNumdict.values()) 
        key = next(key for key, v in modNumdict.items() if v == maxValue)

        return (key) 
