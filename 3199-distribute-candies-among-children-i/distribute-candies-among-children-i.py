class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        
        for i in range(max(0, n - limit * 2), min(limit, n) + 1):
            rem = n - i 
            
            min_qty = max(0, rem - limit) 

            max_qty = min(rem, limit)

            ans += max_qty - min_qty + 1
            
        return ans