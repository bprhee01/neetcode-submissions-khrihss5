# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        targetI = l - n

        #case its at the start of list
        print(targetI)
        if targetI == 0:
            return head.next

        count = 0
        prev, curr = None, head
        while count != targetI:
            print(count,targetI, curr.val)
            tmp = curr
            curr = curr.next
            prev = tmp
            count += 1
        # print(prev.val, curr.val)
        prev.next = curr.next
        curr = None
        return head