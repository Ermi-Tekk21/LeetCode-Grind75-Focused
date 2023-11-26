class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            s=str(i)
            counter=0
            for j in range(len(s)):
                if(int(s[j])!=0):
                    if(i%(int(s[j])))==0:
                        counter+=1
            if(counter==len(s)):
                ans.append(int(s))
        return ans