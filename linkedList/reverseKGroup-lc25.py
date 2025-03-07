# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reverse nodes of the list k at a time
        # you really need to draw out the LL for this problem to fully understand it ;(((
        # initialize dummy node
        dummy = ListNode(val=0, next=head)
        groupPrev = dummy

        while True:
            # kth is the last node in our current group
            kth = self.getKth(groupPrev, k)
            # we don't have enough k nodes to reverse in the remaining LL
            if not kth:
                return dummy.next
            
            # the node after the group that we reverse
            groupNext = kth.next

            # reverse group
            # set curr to the first node in our current group
            # note that prev != None here
            # since we want to combine all the reversed groups together
            # we have to set the prev ptr to the first group after our current group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # pretty complicated
            # tmp is the first node in our current group
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next

    def getKth(self, curr, k): # iterate k times
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr