# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        n1 = ""
        n2 = ""
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        
        print(n1, n2)
        n1 = n1[::-1]
        n2 = n2[::-1]

        result = int(n1) + int(n2)
        backtostring = (str(result))[::-1]
        print(backtostring)
        res = root
        for i in range(len(backtostring)):
            res.val = int(backtostring[i])
            if i + 1 != len(backtostring):
                res.next = ListNode()
            else:
                res.next = None
            res = res.next
        res = None
        return root
            
