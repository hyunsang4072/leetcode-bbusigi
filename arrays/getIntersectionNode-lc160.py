def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # working soln1
    # seen = {}

    # curr = headA
    # while curr:
    #     if curr not in seen:
    #         seen[curr] = curr.val
    #     curr = curr.next
    
    # curr2 = headB
    # while curr2:
    #     if curr2 in seen:
    #         return curr2
    #     curr2 = curr2.next
    
    # return None

    # optimized & simple
    l1, l2 = headA, headB

    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    
    return l1