# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    ########### Optimal && More Concise Soln. ###########
    # TC: O(m + n)
    # SC: O(1)
    dummy = ListNode()
    curr = dummy

    carry = 0 # b/c addition might have carry
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # compute new digit as whole
        val = v1 + v2 + carry # don't forget about the carry
        carry = val // 10 # e.g., 13 // 10 = 1
        val = val % 10 # e.g., 13 % 10 = 3
        curr.next = ListNode(val)

        # update ptrs -- you still need to update each LL
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next
    
    ########### Working Soln. ###########
    # def get_digit(number, n):
    #     return number // 10**n % 10
    # s1, s2 = 0, 0
    # first, second = l1, l2

    # multiplier = 1
    # while first:
    #     s1 += (first.val * multiplier)
    #     multiplier *= 10
    #     first = first.next
    
    # multiplier = 1
    # while second:
    #     s2 += (second.val * multiplier)
    #     multiplier *= 10
    #     second = second.next
    
    # # 807
    # summ = s1 + s2

    # c = 0
    # dummy = ListNode(0)
    # curr = dummy

    # length = len(str(summ)) # avoid repeated work
    # while c < length:
    #     val = get_digit(summ, c)
    #     curr.next = ListNode(val=val)
    #     curr = curr.next
    #     c += 1
    
    # return dummy.next