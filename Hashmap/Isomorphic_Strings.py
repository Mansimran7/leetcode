class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dic1 = {}
        
        s1 = ""
        for i in range(0, len(s)):
            if s[i] not in dic1:
                if (t[i] in list(dic1.values())):
                    return False
                dic1[s[i]] = t[i]
            
            s1 += dic1[s[i]]
        print(s1)
        if(s1 == t):
            return True
        else:
            return False
