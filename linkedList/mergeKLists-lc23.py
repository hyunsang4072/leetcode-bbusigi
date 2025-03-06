# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    # Divide and Conquer approach (iteration)
    # TC: O(n*logk), where n = total number of LL nodes across k lists
    # SC: O(k), where k = total number of lists

    # edge cases: nothing to merge; empty list(s)
    if not lists or len(lists) == 0: # lists = [] or lists = [[]]
        return None
    
    # otherwise, merge two lists at a time until len(lists) == 1
    while len(lists) > 1: # keep shrinking the lists
        mergedList = []

        # we look at two lists at a time
        for i in range(0, len(lists), 2): # step size is 2
            l1 = lists[i] # always exists
            # it's ok to have l2 = None since we are just merging l1 and None in that case
            # we don't want to go outside of bounds
            l2 = lists[i + 1] if (i + 1) < len(lists) else None

            # merge two lists and append it to res list
            # until we end up with just one big sorted list
            mergedList.append(self.merge(l1, l2))
        
        # we need this so that we don't get caught in infinite loop
        lists = mergedList
    
    return lists[0] # one big sorted list

# implement merge 2 sorted LL
def merge(self, l1, l2) -> Optional[ListNode]:
    dummy = node = ListNode()

    while l1 and l2:
        if l1.val <= l2.val:
            node.next = ListNode(val=l1.val)
            node = node.next
            l1 = l1.next
        else:
            node.next = ListNode(val=l2.val)
            node = node.next
            l2 = l2.next
    
    node.next = l1 or l2

    return dummy.next