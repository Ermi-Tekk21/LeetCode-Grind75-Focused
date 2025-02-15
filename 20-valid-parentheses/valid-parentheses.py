class Solution:
    def isValid(self, s: str) -> bool:
        pair_of_char = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        
        
        for char in s:
            if char in pair_of_char.keys():
                stack.append(char) 
            else :
                if not stack or pair_of_char[stack.pop()] != char:
                    return False
        if stack :
            return False
        
        
        return True
