class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        # O(n) solution gives TLE
        # count = 1
        # if n > 0:
        #     for i in range(n):
        #         count *= x
        #     return count
        
        # elif n < 0:
        #     n = -1*n
        #     for i in range(n):
        #         count /=x
        #     return count

        # else:
        #     return 1
        
        # O(logn) solution 

        def exp1(x, exp):
            if exp == 0:
                return 1
            elif exp%2 == 0:
                return exp1(x * x, exp//2)
            else:
                return x * exp1(x * x, (exp-1)//2)
        
        ans = exp1(x, abs(n))

        if n>0:
            return ans
        else:
            return 1/ans
