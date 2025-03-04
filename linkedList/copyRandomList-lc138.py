class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # two-pass soln. using HashMap
    # TC: O(n)
    # SC: O(1)

    # first pass: iterate through each node in original to create a copy node
    # create a hashmap; for each original node, map it to the corresponding copy node
    traveler = head
    nodes = {}

    while traveler:
        nodes[traveler] = Node(val=traveler.val)
        traveler = traveler.next
    
    # second pass: now that we have a hashmap of each node of both original and copy LL
    # start building random pointer for each copy node
    for n in nodes:
        c = nodes[n] #copy
        c.random = nodes[n.random] if n.random != None else None
        c.next = nodes[n.next] if n.next != None else None
    
    return nodes[head] if head else None

    # soln. that only works if original copy doesn't contain any duplicate vals...
    # curr = head
    # pointers = {}

    # c = 0
    # while curr:
    #     pointers[c] = curr.random.val if curr.random else None
    #     curr = curr.next
    #     c += 1
    
    # dummy = ListNode(0)
    # traveler = dummy
    # curr = head
    # copies = {}

    # while curr:
    #     traveler.next = ListNode(val=curr.val)
    #     traveler = traveler.next
    #     copies[curr.val] = traveler
    #     curr = curr.next
    
    # traveler = dummy.next

    # c = 0
    # while traveler:
    #     traveler.random = copies[pointers[c]] if pointers[c] != None else None
    #     c += 1
    #     traveler = traveler.next
    
    # return dummy.next