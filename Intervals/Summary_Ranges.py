class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        
        l1 = [] 
        for i in nums:
            if len(l1) == 0 or (len(l1) == 1 and l1[0]+1 == i):
                l1.append(i)
            elif len(l1) == 1 and l1[0]+1 < i:
                ans.append(str(l1[0]))
                l1=[]
                l1.append(i)
            elif len(l1) == 2 and l1[1]+1 == i:
                l1[1] = i
            elif len(l1) == 2 and l1[1]+1 < i:
                ans.append(str(l1[0]) + "->" + str(l1[1]))
                l1=[]
                l1.append(i)
        
        if len(l1) == 1:
            s = str(l1[0])
            ans.append(s)
        elif len(l1) == 2:
            s = str(l1[0]) + "->" + str(l1[1])
            ans.append(s)
        return ans
