# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1_v = 0
        coef = 1
        curr = l1
        while curr:
            l1_v += curr.val * coef
            curr = curr.next
            coef *= 10

        l2_v = 0
        coef = 1
        curr = l2
        while curr:
            l2_v += curr.val * coef
            curr = curr.next
            coef *= 10

        ans = l1_v + l2_v
        lis = list(str(ans))[::-1]
        head = curr = ListNode(lis[0])
        for x in lis[1:]:
            curr.next = ListNode(x)
            curr = curr.next
        return head
