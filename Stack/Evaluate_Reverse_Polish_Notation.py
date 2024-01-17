class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        for i in tokens:
            if i.isalnum() or ('-' in i and len(i) > 1):
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+": stack.append(a+b)
                elif i == "-": stack.append(b-a)
                elif i == "*": stack.append(a*b)
                else: stack.append(int(b/a))
            
        return stack[-1]
        
