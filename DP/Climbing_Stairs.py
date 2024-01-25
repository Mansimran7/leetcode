class Solution:
    def climbStairs(self, n: int) -> int:
        
        l = [-1]*(n+1)
        def climbing(curr_step):
            if curr_step == n:
                return 1
            elif curr_step > n:
                return 0
            else:
                if l[curr_step+1] != -1:
                    a = l[curr_step+1]
                else:
                    a=climbing(curr_step+1)
        
                if curr_step + 2 < n and l[curr_step+2] != -1:
                    b = l[curr_step+2]
                else:
                    b = climbing(curr_step+2)
                l[curr_step] = a+b
                return l[curr_step]
        
        return climbing(0)
 
