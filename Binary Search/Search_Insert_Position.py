class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        if target < nums[0]:
            return 0
        elif target > nums[n-1]:
            return n
        
        low = 0
        high = n-1 

        while high >= low:
            mid = (high + low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if target > nums[mid]:
            return mid + 1
        else:
            return mid

        
