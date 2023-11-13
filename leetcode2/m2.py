# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        remain = 0
        fake = ListNode(-1)
        cur = fake
        while l1 or l2 or remain:
            v1 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            v2 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            res = v1 + v2 + remain
            if res >= 10:
                remain = 1
            else:
                remain = 0
            cur.next = ListNode(res % 10)
            cur = cur.next
        return fake.next
