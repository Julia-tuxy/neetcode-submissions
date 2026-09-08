# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        cnt = 0

        while cur:
            cnt += 1
            cur = cur.next
        
        target = cnt - n
        dummy = ListNode(next = head)
        cur = dummy

        while target > 0:
            cur = cur.next
            target -= 1
        
        temp = cur.next.next
        remove = cur.next
        cur.next = temp
        remove.next = None

        return dummy.next
