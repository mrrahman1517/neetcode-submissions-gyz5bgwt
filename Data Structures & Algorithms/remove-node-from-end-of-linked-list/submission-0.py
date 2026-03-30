# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        l = 0
        while node:
            l += 1
            node = node.next
        # l is the length of list
        #
        node = head
        prev = None
        curr = head
        m = l - n
        if m == 0:
            return head.next
        while m > 0:
            m -= 1
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head
        