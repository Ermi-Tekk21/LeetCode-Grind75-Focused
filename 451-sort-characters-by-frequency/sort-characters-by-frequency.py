from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d =  Counter(s)
        l = list(sorted(d,key = d.get,reverse = True))
        return ''.join(i*d[i] for i in l)
        