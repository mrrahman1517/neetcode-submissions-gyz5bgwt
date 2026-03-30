# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self, list1, list2):
        # merge 2 lists and return head
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) ==0:
            return None
        #merge pairs of lists and create new list of lists to merge
        currLists = lists
        newLists = []
        i = 0
        while len(currLists) > 1:
            newLists = []
            i = 0
            while i + 1 < len(currLists):
                newLists.append(self.mergeList(currLists[i], currLists[i+1]))
                i += 2

            if len(currLists) % 2 == 1:
                # add one last list
                newLists.append(currLists[len(currLists) - 1])

            currLists = newLists

        return currLists[0]
        