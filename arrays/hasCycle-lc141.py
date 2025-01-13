def hasCycle(self, head: Optional[ListNode]) -> bool:
    dummy = ListNode(next=head)
    slow, fast = dummy, dummy

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False