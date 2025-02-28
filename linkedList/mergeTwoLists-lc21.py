# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    # concise soln.
    # TC: O(n + m)
    # SC: O(1)
    # dummy is the return value
    # node is the current node that helps us iterate through both LLs
    # to create a merged sorted list
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next
    
    # because we might have some leftover nodes from either of LLs
    node.next = list1 or list2

    return dummy.next

    ################################################
    # lengthy and slightly slower soln
    # -> slower b/c we create a new LL node each iteration
    # dummy = ListNode()
    # curr = dummy

    # while list1 and list2:
    #     nxt = ListNode()
    #     curr.next = nxt
    #     if list1.val <= list2.val:
    #         nxt.val = list1.val
    #         list1 = list1.next
    #     else:
    #         nxt.val = list2.val
    #         list2 = list2.next
    #     curr = curr.next
    
    # while list1:
    #     nxt = ListNode(val=list1.val)
    #     curr.next = nxt
    #     list1 = list1.next
    #     curr = curr.next
    
    # while list2:
    #     nxt = ListNode(val=list2.val)
    #     curr.next = nxt
    #     list2 = list2.next
    #     curr = curr.next
    
    # return dummy.next