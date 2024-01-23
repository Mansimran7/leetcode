# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        l = []

        def calcSum(root, val):
            val = val*10 + root.val
            if not root.left and not root.right:
                l.append(val)
            elif not root.right:
                calcSum(root.left, val)
            elif not root.left:
                calcSum(root.right, val)
            else:
                calcSum(root.left, val)
                calcSum(root.right, val)
        
        calcSum(root, 0)

        return sum(l)
