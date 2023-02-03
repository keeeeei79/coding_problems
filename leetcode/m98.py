# class Solution:
#     def is_valid(self, root: Optional[TreeNode], low: int, high: int) -> bool:
#         if not root:
#             return True
#         check_left = root.val > root.left.val > low if root.left else True
#         check_right = high > root.right.val > root.val if root.right else True
#         left_valid = self.is_valid(root.left, low, root.val)
#         right_valid = self.is_valid(root.right, root.val, high)
#         return check_left and check_right and left_valid and right_valid

#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self.is_valid(root, -inf, inf)


# 自分自身がlow<self<highを満たしてるかだけをチェックする方が速い
class Solution:
    def is_valid(self, root: Optional[TreeNode], low: int, high: int) -> bool:
        if not root:
            return True
        if low >= root.val or high <= root.val:
            return False
        return self.is_valid(root.left, low, root.val) and self.is_valid(
            root.right, root.val, high
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, -inf, inf)
