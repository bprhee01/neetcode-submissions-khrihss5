# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr, fast = head, head.next

        while curr and fast and fast.next:
            if curr == fast:
                return True
            curr = curr.next
            fast = fast.next.next
        
        return False