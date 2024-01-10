class Solution:
    def threeSum(self, strs: List[int]) -> List[List[int]]:
        
        strs.sort()
        l = []
        for i in range(len(strs)):
            if i > 0 and strs[i-1]==strs[i]:
                continue
            k = len(strs)-1
            j = i+1 
            while(j < k):
                s = strs[i] + strs[j] + strs[k]
                if( s == 0):
                    l.append([strs[i], strs[j], strs[k]])  
                    j+=1
                    while strs[j-1] == strs[j] and j<k:
                        j+=1
                elif (s > 0):
                    k-=1
                else:
                    j+=1
        return l
