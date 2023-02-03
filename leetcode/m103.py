class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        left_to_right = True
        while queue:
            cur_lvl_size = len(queue)
            cur_res = [0] * cur_lvl_size  # 配列のサイズを確保する
            for i in range(cur_lvl_size):
                node = queue.popleft()
                idx = i if left_to_right else cur_lvl_size - 1 - i
                cur_res[idx] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_res)
            left_to_right = not left_to_right
        return res
