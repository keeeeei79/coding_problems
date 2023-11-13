from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorderの最初が必ずroot
        # inorderはそれで2つの部分木に分けれる
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        inorder_root_idx = left_tree_length = inorder.index(root.val)

        left_tree_inorder = inorder[:inorder_root_idx]
        right_tree_inorder = inorder[inorder_root_idx + 1 :]

        left_tree_preorder = preorder[1 : left_tree_length + 1]
        right_tree_preorder = preorder[left_tree_length + 1 :]

        root.left = self.buildTree(left_tree_preorder, left_tree_inorder)
        root.right = self.buildTree(right_tree_preorder, right_tree_inorder)

        return root


s = Solution()
s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
