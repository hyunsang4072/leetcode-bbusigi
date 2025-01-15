def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # 1. use fast&slow algo to find middleNode(=slowPtr)
    # 2. starting from middleNode, reverse the direction of ptrs until end
    # 3. two ptrs to iteratively check if palindrome: dummy=head, prev=end
    if not head:
        return False
    
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # fast&slow algo to find middleNode
    # slow at middle; fast at end
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    
    # slow at end of reversed LL
    dummy = head
    while prev:
        if dummy.val != prev.val:
            return False
        dummy = dummy.next
        prev = prev.next
    
    return True