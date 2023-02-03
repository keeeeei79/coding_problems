class Solution:
    def get_depth(self, node: TreeNode) -> int:
        level = 1
        if not node.left and not node.right:
            return level
        left_level = level
        right_level = level
        if node.left:
            left_level += self.get_depth(node.left)
        if node.right:
            right_level += self.get_depth(node.right)
        return max([left_level, right_level])

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.get_depth(root)
