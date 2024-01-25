class Solution:
    def rob(self, nums: List[int]) -> int:

        l = [-1] * (len(nums))

        def robbing(count):
            if count == 0:
                l[count] = nums[count]
                return nums[count]
            
            if count == 1:
                l[count] = max(nums[0], nums[1])
                return l[count]


            if l[count] != -1:
                return l[count]
            
            else:
                cost = max(
                    nums[count] + robbing(count - 2),
                    robbing(count - 1)
                )
                l[count] = cost
                return l[count]
        return robbing(len(nums)-1)
        
