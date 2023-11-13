from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [([root], 0)]
        res = []
        fromRight = False
        while queue:
            nodes, level = queue.pop(0)
            next_nodes = []
            res.append([0] * len(nodes))
            for i in range(len(nodes)):
                node = nodes[i]
                res_i = len(nodes) - 1 - i if fromRight else i
                res[level][res_i] = node.val
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if next_nodes:
                queue.append((next_nodes, level + 1))
            fromRight = not fromRight
        return res


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

s = Solution()
print(s.zigzagLevelOrder(t1))
