class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            temp = 0
            for x in str(n):
                temp += int(x)**2
            n = temp
            if n == 1:
                return True
            if n in s:
                return False
            
            s.add(n)