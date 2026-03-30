class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        second = self.reverseList(slow.next)
        slow.next = None

        # 3. Merge two halves
        first = head
        while second:
            n1 = first.next
            n2 = second.next

            first.next = second
            second.next = n1

            first = n1
            second = n2