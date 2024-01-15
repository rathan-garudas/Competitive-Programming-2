class Solution:
    def stringCode(self, s):
        primeMap = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        code = 1
        for i in s:
            code *= primeMap[(ord(i) - ord('a'))]
        return code
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq={}

        for i in strs:
            code = self.stringCode(i)
            if code in freq:
                freq[code].append(i)
            else:
                freq[code] = [i]

        return list(freq.values())
