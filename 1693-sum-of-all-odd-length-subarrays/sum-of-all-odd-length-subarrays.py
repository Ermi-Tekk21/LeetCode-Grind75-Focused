class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        catch_sum = []
        for k in range(1, len(arr)+1, 2):
            for i in range (len(arr)-k+1):
                catch_sum.append(sum(arr[i:i+k]))
            
        return (sum(catch_sum))