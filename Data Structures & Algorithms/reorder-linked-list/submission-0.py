# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # algorithm
        # find middle of list using slow-fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        # reverse second half of list

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # merge first half and reverse of second half
        # prev points to start of reverse of second list
        l1 = head
        l2 = prev
        while l1 and l2:
            t1 = l1.next
            l1.next = l2
            t2 = l2.next
            l2.next = t1
            l1 = t1
            l2 = t2