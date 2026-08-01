# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, list1: Optional[ListNode]):
        while list1:
            print(list1.val, end=" ")
            list1 = list1.next
        print("")
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # self.printList(list1)
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        #Trying to get the lowest num as root is not stupid I think
        main = None
        insert = None
        root = None

        if list1.val > list2.val:
            main = list2
            insert = list1
        elif list1.val <= list2.val:
            main = list1
            insert = list2
        root = main
        self.printList(main)
        self.printList(insert)
        while insert:
            #at first it will always be bigger
            if main.next == None:
                main.next = insert
                break
            if insert.val >= main.val:
                if insert.val > main.next.val:
                    main = main.next
                else:
                    #bigger than main but less than main.next, AKA perfect !
                    tmp = insert.next
                    insert.next = main.next
                    main.next = insert
                    insert = tmp
            elif insert.val < main.val:
                print("you fucked up")
        self.printList(root)
        return root





