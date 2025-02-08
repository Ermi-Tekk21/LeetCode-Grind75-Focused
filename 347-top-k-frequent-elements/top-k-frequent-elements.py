class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        catch = set(nums)
        top = {}

        for i in catch:
            top[i] = nums.count(i)

        sortedTop = sorted(top.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(sortedTop[i][0])  

        return(ans)  
