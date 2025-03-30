class Solution:
    mem = {}
    def fib(self, x):
        if x < 2: 
            return 1
        if x in self.mem:
            return self.mem[x]

        tmp = 1
        ans = 2
        for i in range(3, x+1):
            next_val = ans+tmp
            tmp = ans
            ans = next_val
        self.mem[x] = ans
        return self.mem[x]

    def numDecodings(self, s: str) -> int:
        if s[0]=="0": 
            return 0

        # validate s
        n = len(s)
        for i in range(1, n):
            if s[i]=="0" and s[i-1] not in ["1", "2"]: 
                return 0
        
        ans, count = 1, 0
        for i in range(n):
            if s[i]=="1" or s[i]=="2": 
                count+=1

            # stop
            elif i>0:
                # decrease count for 0's
                if s[i]=="0": 
                    count-=1
                # include if they can make a valid character
                elif s[i-1]=="1" or ( "2" < s[i] < "7" and s[i-1]=="2"):
                    count+=1

                ans *= self.fib(count)
                count=0

        ans *= self.fib(count)

        return ans
                    
                