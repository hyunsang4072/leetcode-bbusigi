# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # c1 = 1
    # dummy = head.next

    # while dummy:
    #     c1 += 1
    #     dummy = dummy.next

    # if c1 == n:
    #     return head.next
    
    # # of nodes in LL = c1
    # tummy = head
    # c2 = 1
    # while c2 != (c1-n):
    #     tummy = tummy.next
    #     c2 += 1
    
    # if tummy.next:
    #     tummy.next = tummy.next.next

    # return head

    # slow, fast ptrs
    dummy = ListNode(next=head)
    fast = dummy
    slow = dummy

    for i in range(n):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # remove n-th node
    if slow.next:
        slow.next = slow.next.next

    return dummy.next