class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        l,r=0,len(nums)-1

        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                #left sorted
                if nums[l] <= target and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                #right sorted
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1