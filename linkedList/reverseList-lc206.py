# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    curr = head

    while head:
        head = head.next
        curr.next = prev
        prev = curr
        curr = head
    
    return prev