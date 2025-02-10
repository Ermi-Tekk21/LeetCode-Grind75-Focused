class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = str(x)
        size = len(nums)
        rPtr = size - 1
        
        for i in range (size // 2):
            if nums[i] != nums[rPtr - i]: 
                return False
        return True