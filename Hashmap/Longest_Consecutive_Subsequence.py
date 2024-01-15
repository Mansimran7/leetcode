class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums1 = set(nums)
        visited = set()
        totalMax = 0
        for num in nums:
            if num - 1 not in nums1:
                maxC = 1 
                visited.add(num)
                num+=1

                while num in nums1 and num not in visited:
                    maxC+=1 
                    visited.add(num)
                    num+=1
                totalMax = max(maxC, totalMax)

        return totalMax            
