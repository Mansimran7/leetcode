class Solution:
    def mySqrt(self, x: int) -> int:

        low = 0 
        high = x

        while (high >= low):
            mid = (high+low)//2 
            if mid * mid <= x and (mid+1) * (mid+1) > x:
                return mid
            elif (mid+1) * (mid+1) <= x:
                low = mid+1
            else:
                high = mid
