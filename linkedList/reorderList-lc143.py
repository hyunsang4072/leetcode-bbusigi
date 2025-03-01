# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # now, slow pointer at the middle of LL

    # reverse LL from slow to end
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    # final step is to merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    # we don't have to return anything since this algo is done in-place