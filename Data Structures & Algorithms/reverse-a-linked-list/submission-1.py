# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        if not head:
            return head
        while curr and curr.next:
            temp = curr.next # temp = Node(1,2)
            curr.next = prev # curr =Node(0, None), prev = None
            prev = curr # prev = Node(0,none)
            curr = temp # curr =Node(1, 2)
        curr.next =prev
        return curr
