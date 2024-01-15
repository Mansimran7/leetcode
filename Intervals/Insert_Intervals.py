class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        l1 = sorted(intervals)

        ans = []
        k=0
        while(k < len(l1)):
            if k!= 0 and ans[len(ans)-1][1] >= l1[k][0]:
                newL = [min(ans[len(ans)-1][0], l1[k][0]), max(ans[len(ans)-1][1], l1[k][1])]
                ans[len(ans)-1] = newL
            else:
                ans.append(l1[k])
            k+=1
            
        return ans
