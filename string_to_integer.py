class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        res = 0
        sign = 1
        i = 0
        
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            if res > (MAX_INT - digit) // 10:
                return MAX_INT if sign == 1 else MIN_INT
            
            res = res * 10 + digit
            i += 1
            
        return max(MIN_INT, min(MAX_INT, res * sign))

        
