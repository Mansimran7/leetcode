class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dic = {}
        l = []
        l = s.split(' ')

        if len(l) != len(pattern):
            return False
            
        for i in range(0, len(l)):
            if l[i] not in dic:
                if pattern[i] in list(dic.values()):
                    return False
                dic[l[i]] = pattern[i]
            
            elif dic[l[i]] != pattern[i]:
                return False           
        return True
