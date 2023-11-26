class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        x=min(len(word1),len(word2))
        for i in range(x):
            ans.append(word1[i])
            ans.append(word2[i])
        left_word1=word1[x:]
        left_word2=word2[x:]
        ans.extend(left_word1)
        ans.extend(left_word2)
        return "".join(ans)