from typing import List, Dict, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    inorder: List[int]
    preorder: List[int]
    inhash: Dict[int, int]
    preorder_idx: int

    def extract_root(self, left: int, right: int) -> Optional[TreeNode]:
        # left, rightは部分配列の両端のindexを表す
        if left > right:
            return None
        root_val = self.preorder[self.preorder_idx]
        root = TreeNode(root_val)
        self.preorder_idx += 1  # preorderをずらしていけばnodeを辿れる

        root.left = self.extract_root(left, self.inhash[root_val] - 1)
        root.right = self.extract_root(self.inhash[root_val] + 1, right)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder  # 本当はいらないがdebug用
        self.preorder = preorder
        self.inhash = {}
        for i, v in enumerate(inorder):
            self.inhash[v] = i
        self.preorder_idx = 0
        return self.extract_root(0, len(preorder) - 1)


s = Solution()
preorder = [3, 9, 1, 2, 20, 15, 7]
inorder = [1, 9, 2, 3, 15, 20, 7]
s.buildTree(preorder, inorder)
