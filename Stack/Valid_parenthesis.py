class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            elif i == "}":
                if stack and stack[len(stack)-1] == "{":
                    stack.pop(len(stack)-1)
                else:
                    return False
            elif i == "]":
                if stack and stack[len(stack)-1] == "[":
                    stack.pop(len(stack)-1)
                else:
                    return False
            elif i == ")":
                if stack and stack[len(stack)-1] == "(":
                    stack.pop(len(stack)-1)
                else:
                    return False
        if len(stack) != 0:
            return False
        
        return True
        
