class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            if not node.left and not node.right:
                return level
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        return 0
