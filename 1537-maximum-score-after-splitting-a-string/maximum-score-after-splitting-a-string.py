class Solution:
    def maxScore(self, s: str) -> int:
        count_zeros = 0
        count_ones = s.count('1')
        max_score = 0
        for i in range(len(s) - 1):  
            if s[i] == '0':
                count_zeros += 1
            else:
                count_ones -= 1
            max_score = max(max_score, count_zeros + count_ones)
        
        return max_score
