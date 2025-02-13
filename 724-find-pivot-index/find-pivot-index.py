class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]

        for i in range (1, len(nums)):
            prefixSum.append(prefixSum[i-1] + nums[i]) 

        for j in range (len(prefixSum)):
            if j == 0:
                if (prefixSum[-1]-prefixSum[j] == 0):
                    return 0
            else: 
                if (prefixSum[j-1] - (prefixSum[-1]-prefixSum[j]) == 0):
                    return j
        return -1