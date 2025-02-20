class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        res = sum(cardPoints[n-k:])
        s = res
        for i in range(k):
            s += cardPoints[i]
            s -= cardPoints[-(k-i)]
            res = max(res, s)
        return res