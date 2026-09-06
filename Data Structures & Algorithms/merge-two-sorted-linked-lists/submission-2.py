# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        
        dummy = cur = ListNode(None)

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                temp = cur1.next
                cur.next = cur1
                cur = cur1
                cur1 = temp
            else:
                temp = cur2.next
                cur.next = cur2
                cur = cur2
                cur2 = temp
        
        if cur1:
            cur.next = cur1
        
        if cur2:
            cur.next = cur2
        
        return dummy.next
                