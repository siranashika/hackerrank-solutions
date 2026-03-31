class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()       
        words.reverse()       
        ans = " ".join(words)       
        return ans
