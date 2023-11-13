from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # e141はfastはhead.nextとしていたがここではslowとfastが一致した場所からcycleの始まりまでの距離と
        # headからcycleの始まりまでの距離が同じことを利用するため、fastもheadとする
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head


l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

s = Solution()
s.detectCycle(l1)
