def hasCycle(self, head: Optional[ListNode]) -> bool:
    # TC: O(n)
    # SC: O(1)
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False