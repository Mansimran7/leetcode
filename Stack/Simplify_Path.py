class Solution:
    def simplifyPath(self, path: str) -> str:

        l = path.split('/')
        stack = []
        ans = ""
        for i in l:
            if len(i) != 0 and i != "." and i !=  "..":
                stack.append(i)
            elif i == ".." and stack:
                stack.pop(len(stack)-1)

        for i in stack:
            ans += "/" + i

        return ans if ans else "/"
