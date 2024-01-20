class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        hMap = {}
        hMap[0] = -1
        rSum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                rSum -= 1
            else:
                rSum += 1
            
            if rSum in hMap:
                result = max(result, i - hMap[rSum])
            else:
                hMap[rSum] = i
        
        return result