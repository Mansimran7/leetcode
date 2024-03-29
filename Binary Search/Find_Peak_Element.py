class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        low = 0 
        high = len(nums) - 1

        if len(nums) == 1:
            return 0

        while (low <= high):
            mid = (low + high)//2

            if mid == len(nums) - 1:
                return mid
            
            elif mid == 0 and nums[mid] > nums[mid+1]:
                return mid
             
            elif nums[mid] <= nums[mid+1]:
                low = mid + 1
            
            elif nums[mid] <= nums[mid-1]:
                high = mid - 1
            else:
                return mid
        

        
