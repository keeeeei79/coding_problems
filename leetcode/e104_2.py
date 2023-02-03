class Solution:
    def get_depth(self, node: TreeNode, level: int) -> int:
        if not node.left and not node.right:
            return level
        left_level = level
        right_level = level
        if node.left:
            left_level = self.get_depth(node.left, level + 1)
        if node.right:
            right_level = self.get_depth(node.right, level + 1)
        return max([left_level, right_level])

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.get_depth(root, 1)
