class Solution:
    def trailingZeroes(self, n: int) -> int:
        

        # O(n) solution 
        
        # count = 0 

        # for i in range(5, n+1, 5):
            
        #     if i%3125 == 0:
        #         count += 5
        #     elif i%625 == 0:
        #         count += 4
        #     elif i%125 == 0:
        #         count += 3
        #     elif i%25 == 0:
        #         count += 2
        #     elif i%5 == 0:
        #         count += 1
            
        #     print(count, i)
        # return count



        # O(logn) solution 

        count = 0 
        res = 5
        while (res <= n):
            count += n//res
            res *=5 
        
        return count
