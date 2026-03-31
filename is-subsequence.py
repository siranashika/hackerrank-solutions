class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n_s = len(s)
        n_t = len(t)        
        while i < n_s and j < n_t:
            if s[i] == t[j]:
                i = i + 1
            j = j + 1           
        if i == n_s:
            return True
        else:
            return False
