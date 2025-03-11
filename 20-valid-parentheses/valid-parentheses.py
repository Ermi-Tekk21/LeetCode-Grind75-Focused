class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {'{': '}', '[': ']', '(': ')'}
        store_open = []
        
        for char in s:
            if char in hash_table:  
                store_open.append(hash_table[char])
            else: # closing bracket
                if not store_open or char != store_open.pop():
                    return False
        
        return not store_open