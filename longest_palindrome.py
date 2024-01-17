class Solution:
    def longestPalindrome(self, s: str) -> int:
        paliSet = set()
        res = 0
        for i in range(len(s)):
            if s[i] in paliSet:
                res += 2
                paliSet.remove(s[i])
            else:
                paliSet.add(s[i])
        
        if len(paliSet) != 0:
            res += 1
        
        return res