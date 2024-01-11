class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(t) != len(s)):
            return False
        dic = {}
        
        for i in t:
            if i not in dic:
                dic[i] = 0 
            dic[i]+=1

        for i in s:
            if i not in dic:
                return False
            dic[i]-=1
            if dic[i] < 0:
                return False

        return True    
        
