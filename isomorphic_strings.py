class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdic = {}
        tset = set()
        for i in range(len(s)):

            if s[i] not in sdic:
                if t[i] in tset:
                    return False
                else:
                    sdic[s[i]] = t[i]
                    tset.add(t[i])
            else:
                if sdic[s[i]] != t[i]:
                    return False
        
        return True