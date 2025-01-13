def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    # working soln1
    # nxt = node.next
    # curr = node

    # while nxt.next:
    #     curr.val = nxt.val
    #     curr = curr.next
    #     nxt = curr.next
    
    # curr.val = nxt.val
    # curr.next = None

    # more clean code
    node.val = node.next.val
    node.next = node.next.next