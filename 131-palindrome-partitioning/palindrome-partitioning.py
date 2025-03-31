class Solution:
    def partition(self, s: str) -> List[List[str]]:


        def dfs(ind,arr):
            if ind == len(s):
                res.append(arr[:])
                return

            
            for i in range(ind,len(s)):
                if _ispal(ind,i):
                    arr.append(s[ind:i+1])
                    dfs(i+1,arr)
                    arr.pop()



        def _ispal(start,end):

            while start <= end:
                if s[start] != s[end]:
                    return False
                
                start+=1
                end-=1

            return True



        res = []
        dfs(0,[])

        return res
        