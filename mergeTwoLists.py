# python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        preHead = ListNode(-1)
        p1 = l1
        p2 = l2
        cur = preHead

        while p1 != None and p2 != None:
            if p1.val < p2.val:
                cur.next = p1
                cur = p1
                p1 = p1.next

            else:
                cur.next = p2
                cur = p2
                p2 = p2.next

        if p1:
            cur.next = p1

        if p2:
            cur.next = p2

        return preHead.next