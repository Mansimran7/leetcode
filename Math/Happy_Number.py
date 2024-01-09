class Solution:
    def isHappy(self, n: int) -> bool:

        def sqrtSum(n: int):
            sum1 = 0 
            while(n>0):
                sum1 += (n%10)**2
                n //= 10
            return sum1
 
        old_n = set()
        while(n != 1):
            n = sqrtSum(n)
            if n in old_n:
                return False
            old_n.add(n)
        return True
        
