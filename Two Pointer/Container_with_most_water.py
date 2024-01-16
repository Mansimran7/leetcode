class Solution:
    def maxArea(self, h: List[int]) -> int:

        p1 = 0 
        p2 = len(h)-1

        curMax = 0 

        while(p1 < p2):
            curMax = max(curMax, (p2-p1) * min(h[p1], h[p2]))
            if h[p1] <= h[p2]:
                p1+=1
            else:
                p2-=1            
        
        return curMax
