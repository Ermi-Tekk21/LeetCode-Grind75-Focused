class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i<j  and nums[i]==nums[j]):
                    answer.append((i,j))
        return len(answer)