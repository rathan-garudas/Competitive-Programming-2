class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        patternDic = {}
        wordSet = set()

        for i in range(len(pattern)):

            if pattern[i] not in patternDic:
                patternDic[pattern[i]] = words[i]
                if words[i] in wordSet:
                    return False
                wordSet.add(words[i])
            else:
                if patternDic[pattern[i]] != words[i]:
                    return False
        return True