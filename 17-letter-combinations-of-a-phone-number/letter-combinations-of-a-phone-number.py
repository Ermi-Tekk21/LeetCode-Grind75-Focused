from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 
                  6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        res, sol = [], []

        if digits == "":
            return []

        def dfs(i):
            if i == len(digits):
                res.append("".join(sol))
                return

            for char in keypad[int(digits[i])]:
                sol.append(char)
                dfs(i + 1)
                sol.pop()  # Backtrack

        dfs(0)
        return res