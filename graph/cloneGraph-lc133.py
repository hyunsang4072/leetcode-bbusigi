"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # use hashMap to get a mapping between original -> copy
        oldToNew = {} # {old: new}

        # must check
        if not node:
            return None
        
        def dfs(n): # take in node -> return a copy of that node
            if n in oldToNew:
                return oldToNew[n]
            
            # otherwise, make a copy and cache
            copy = Node(n.val)
            oldToNew[n] = copy

            # make a copy of each neighbor in original node
            # ensure that it's added to copy's neighbor
            for nei in n.neighbors:
                neighbor = dfs(nei)
                copy.neighbors.append(neighbor)
            
            return copy
        
        return dfs(node)
