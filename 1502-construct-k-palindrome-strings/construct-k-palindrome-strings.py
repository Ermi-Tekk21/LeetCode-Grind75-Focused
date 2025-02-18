class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        s1={}
        for i in s:
            if i in s1:
                s1[i]+=1
            else:
                s1[i]=1
        c=0
        for i in s1:
            if s1[i]%2!=0:
                c+=1
        if c>k:
            return False
        else:
            return True
        
        