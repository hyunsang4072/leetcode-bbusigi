# System Design Question!!!

class Node: # doubly LL
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # The idea is to have the hashMap and doubly LL
    # hashMap is used so that we can retrieve some node in O(1) time
    # doubly LL is for easily keeping track of LRU and right-most positioned nodes
    # e.g., # prev <-> LRU <-> node1 <-> ... <-> right-most node <-> right

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # {key: node}

        # self.left.next = LRU
        # self.right.prev = MRU
        # self.left and self.right are not actual nodes
        # they help us find the LRU and MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node(middle) from list
    # prev <-> node <-> next becomes:
    # prev <-> next
    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # insert node at right-most position
    # prev <-> right becomes:
    # prev <-> node <-> right
    def insert(self, node) -> None:
        prev, nxt = self.right.prev, self.right
        nxt.prev, prev.next = node, node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        # {key: node}
        if key in self.cache:
            # we have to remove AND insert since we have to emulate LRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # we have to remove AND insert since we have to emulate LRU
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # create AND update node in hashMap
        self.insert(self.cache[key])

        if len(self.cache) > self.cap: # full cache --> evict LRU node
            # remove from the list and delete the LRU from the hashMap
            lru = self.left.next
            self.remove(lru)
            # del keyword exists in Python to delete some variable or object
            del self.cache[lru.key] # cache = {key: node}

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)