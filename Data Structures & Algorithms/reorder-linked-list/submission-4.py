# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow
        
        cur = middle.next
        middle.next = None

        #reverse
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        second = prev

        first = head 

        while second:
            temp_first = first.next
            first.next = second
            temp_second = second.next
            second.next = temp_first
            first = temp_first
            second = temp_second
        




