class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = a[::-1]
        b = b[::-1]
        c = ""
        la = 0
        lb = 0 
        carry = 0
        while la < len(a) or lb <len(b):
            sum1 = carry
            if la < len(a):
                sum1 += int(a[la])
                la+=1
            
            if lb < len(b):
                sum1 += int(b[lb])
                lb+=1
            
            if sum1 == 0 or sum1 == 1:
                c+= str(sum1)
                carry = 0
            elif sum1 == 2:
                c+= "0"
                carry = 1
            elif sum1 == 3:
                c+= "1"
                carry = 1
            
        
        if carry == 1:
            c+= "1"
        return c[::-1]

        
