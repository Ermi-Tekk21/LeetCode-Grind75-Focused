class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "" 
        for char in s:
            if char.isalpha() or char.isalnum(): 
                new_s += char.lower()

        for i in range(len(new_s) // 2):
            if new_s[i] != new_s[-1-i]:
                return (False)

        return (True)
            