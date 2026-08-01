# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        myLen = 0
        curr = head
        if head == None:
            return []
        while curr:
            curr = curr.next
            myLen += 1
        if myLen == 1:
            return None
        curr = head
        i = 0
        while i < myLen - n - 1:
            curr = curr.next
            i += 1
        if myLen - n - 1 < 0:
            head = head.next
        curr.next = curr.next.next
        return head