# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -inf, inf)

    def isValid(self, root: Optional[TreeNode], left: int, right: int) -> bool:
        if not root:
            return True

        if not left < root.val < right:
            return False

        validLeft = self.isValid(root.left, left, root.val)
        validRight = self.isValid(root.right, root.val, right)
        return validLeft and validRight
