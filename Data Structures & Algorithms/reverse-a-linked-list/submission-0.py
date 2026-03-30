# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head
        curr = head
        prev = None

        # None  1 -> 2 -> None
        while curr and curr.next:
            temp = curr.next #2
            curr.next = prev # 1-> None
            prev = curr #1
            curr = temp #2 
            print(curr.val)

        curr.next = prev

        
        return curr