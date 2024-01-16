# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        def check(root, count):

            if not root.left and not root.right:
                if root.val + count == targetSum:
                    return True
                else:
                    return False
            if not root.left:
                return check(root.right, count+root.val)
            elif not root.right:
                return check(root.left, count+root.val)
            else:
                return check(root.left, count+root.val) or check(root.right, count+root.val)
        
        return check(root, 0)
