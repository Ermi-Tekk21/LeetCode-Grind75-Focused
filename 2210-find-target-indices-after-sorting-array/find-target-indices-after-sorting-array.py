class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range (size) :
            min_idx = i
            for j in range (i, size):
                if nums[min_idx] > nums[j]:   
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        count = []
        for i in range (size):
            if nums[i] == target:
                count.append(i)
            else :
                pass
        return (count)