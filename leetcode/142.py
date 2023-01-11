# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         s = set()
#         while head:
#             if head in s:
#                 return head
#             else:
#                 s.add(head)
#             head = head.next
#         return


class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = (slow.next, fast.next.next)
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            head, slow = head.next, slow.next
        return head
