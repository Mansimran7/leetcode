class Solution:
    def plusOne(self, d: List[int]) -> List[int]:

        n = len(d)-1
        flag = 1 
        while(n>=0 and flag == 1):

            nums = d[n]
            if d[n] <= 8:
                d[n] += 1
                flag = 0 
            else:
                d[n] = 0
                n-=1
        if flag == 1:
            d.insert(0, 1)
        return d
