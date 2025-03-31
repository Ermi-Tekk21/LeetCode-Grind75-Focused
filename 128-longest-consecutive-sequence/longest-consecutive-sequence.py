class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        ans = 1
        consecutive_size = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]: continue
            if nums[i-1] + 1 == nums[i]:
                consecutive_size += 1
            else:
                ans = max(ans, consecutive_size)
                consecutive_size = 1

        ans = max(ans, consecutive_size)
        return ans