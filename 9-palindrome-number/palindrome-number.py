class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        l = len(n)
        res = True
        counter = 0
        odd_route = int((l-1)/2)
        even_route = int((l)/2)
        if l % 2 == 0:
            for i in range(even_route):
                initial_index = i
                back_index = (-1*i)-1
                front = n[initial_index]
                back = n[back_index]
                if front.isdigit() and back.isdigit():
                    if int(front) == int(back):
                        counter += 1
            if counter == even_route:
                res = True
            else:
                res = False
        else:
            for i in range(odd_route):
                initial_index = i
                back_index = (-1*i)-1
                front = n[initial_index]
                back = n[back_index]
                if front.isdigit() and back.isdigit():
                    if int(front) == int(back):
                        counter += 1
            if counter == odd_route:
                res = True
            else:
                res = False

        return res
