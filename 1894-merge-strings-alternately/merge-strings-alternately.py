class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1 + word2)
        word1 = list(word1)
        word2 = list(word2)
        word1.reverse()
        word2.reverse()
        newStr = ""
        
        for i in range(n):
            
            if i % 2 == 0 and word1:
                newStr += word1.pop()
            elif word2: 
                newStr += word2.pop()
        word1.reverse()     
        word2.reverse()     
        newStr += ("").join(word1)
        newStr += ("").join(word2)
        return newStr