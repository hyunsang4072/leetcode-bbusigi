def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # do NOT use hashMap for this problem!!!
    # res = None
    # seen = {}

    # dummy = head
    # while dummy:
    #     node = dummy
    #     if node in seen:
    #         return node
    #     seen[node] = 1
    #     dummy = dummy.next
    
    # return res

    # use fast&slow algo(tortoise) --> optimal        
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # found a cycle
            dummy = head
            while True:
                if dummy == fast:
                    return dummy
                dummy = dummy.next
                fast = fast.next
    
    # no cycle
    return None