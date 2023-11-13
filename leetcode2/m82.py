# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(-1, head)
        prev = fake
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                val = cur.val
                while cur and val == cur.val:
                    cur = cur.next
                prev.next = cur
            else:
                prev = prev.next
                cur = cur.next
        return fake.next
