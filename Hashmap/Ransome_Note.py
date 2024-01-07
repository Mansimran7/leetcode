class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic = {}

        for i in magazine:
            if i not in dic:
                dic[i] = 0 
            dic[i]+=1

        print(dic) 

        for i in ransomNote:
            if i not in dic:
                return False
            dic[i]-=1
            if dic[i] < 0:
                return False
        
        return True
