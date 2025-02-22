class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l = min(len(word1), len(word2))
        for i in range(l):
            res += word1[i] + word2[i]
        return res + word1[l:] + word2[l:]