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

        queue = [(root, targetSum)]
        while queue:
            node, total = queue.pop(0)
            # leafでtargetSum=0ならOK
            if not node.left and not node.right and total == node.val:
                return True
            if node.left:
                queue.append((node.left, total - node.val))
            if node.right:
                queue.append((node.right, total - node.val))
        return False
