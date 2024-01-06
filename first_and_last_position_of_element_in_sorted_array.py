class Solution:
    def searchFirstIndex(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                if mid == low or nums[mid] > nums[mid-1]:
                    return mid
                else:
                    high = mid - 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


    def searchLastIndex(self, nums, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                if mid == high or nums[mid] < nums[mid+1]:
                    return mid
                else:
                    low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
                
            else:
                low = mid + 1
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) == 0:
            return [-1, -1]
        firstIdx = self.searchFirstIndex(nums, target)
        if firstIdx == -1:
            return [-1, -1]
        lastIdx = self.searchLastIndex(nums, firstIdx, len(nums)-1, target)
        return [firstIdx, lastIdx]