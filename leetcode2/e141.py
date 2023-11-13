# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # ウサギと亀アルゴリズム
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        tortoise, hare = head, head.next
        while tortoise != hare:
            if not hare or not hare.next:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
        return True
