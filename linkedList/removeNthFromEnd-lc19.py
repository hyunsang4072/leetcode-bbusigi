# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # two pointers approach
    # TC: O(n)
    # SC: O(1)
    # first will move n times forward
    first = head
    # we make dummy node that's one step before head pointer <-- to avoid edge cases
    # initialize second at dummy
    dummy = ListNode(val=0, next=head)
    second = dummy
    for i in range(n):
        first = first.next
    
    # we move second forward until the first pointer reaches the end(None)
    # this will place second at a desired node
    while first:
        second = second.next
        first = first.next
    
    # we can just skip(=remove) the next of second
    second.next = second.next.next

    return dummy.next