class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]
        low = 0 
        high = len(nums) - 1
        a = -1
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                a = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if a == -1:
            return [-1, -1]
        
        low = 0 
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target and (mid == len(nums) - 1 or target < nums[mid+1]):
                b = mid
                return [a,b]
            elif nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        
