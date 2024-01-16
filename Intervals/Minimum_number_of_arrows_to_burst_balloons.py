class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        l1 = sorted(points)
        ans = []
        k = 0 

        while(k<len(l1)):
            if k == 0:
                ans.append(l1[k])
                k+=1
            elif ans[len(ans)-1][1] >= l1[k][0]:
                newL = [max(ans[len(ans)-1][0], l1[k][0]), min(ans[len(ans)-1][1], l1[k][1])]
                ans[len(ans)-1] = newL
                k+=1
            else:
                ans.append(l1[k])
                k+=1
        return len(ans)
        
