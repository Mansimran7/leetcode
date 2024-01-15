class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        l1 = sorted(intervals)
        k=0
        ans = []
        while(k < len(l1)):
            if k == 0:
                ans.append(l1[k])
                k+=1

            elif ans[len(ans)-1][1] >= l1[k][0]:
                a = min(ans[len(ans)-1][0], l1[k][0])
                b = max(ans[len(ans)-1][1], l1[k][1])
                newL = [a, b]
                ans[len(ans)-1] = newL
                k+=1
            else:
                ans.append(l1[k])
                k+=1
            
        return ans
