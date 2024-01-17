class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        hMap = {}
        hMap[0] = 1
        rSum = 0
        for i in range(len(nums)):
            rSum += nums[i]

            if rSum - k in hMap:
                result += hMap[rSum - k]

            if rSum in hMap:
                hMap[rSum] += 1
            else:
                hMap[rSum] = 1

        return result