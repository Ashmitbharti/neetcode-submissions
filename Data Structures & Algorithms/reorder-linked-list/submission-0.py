class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        second = prev
        first = head

        dummy = ListNode()
        tail = dummy

        while first and second:
            t1 = first.next
            t2 = second.next
            tail.next = first
            tail = tail.next
            tail.next = second
            tail = tail.next
            first = t1
            second = t2
        tail.next = first if first else second