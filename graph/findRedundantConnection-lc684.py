def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # union find w/ path compression (for optimization)
    n = len(edges)
    parent = [i for i in range(n + 1)] # (n + 1) b/c node starts from 1, ..., n
    rank = [1] * (n + 1) # (n + 1) b/c node starts from 1, ..., n

    # find the root parent of node n
    # V = # of nodes
    # E = # of edges
    def find(n): # TC: O(V + (E * a(V)))
        res = n

        while res != parent[res]:
            parent[res] = parent[parent[res]]
            res = parent[res]
        
        return res
    
    # find the root parents of n1, n2
    # union them if possible
    def union(n1, n2): # TC: O(V + (E * a(V)))
        p1, p2 = find(n1), find(n2)

        # already connected to the same root parent
        # => if union n1, n2, result in cycle
        if p1 == p2:
            return False
        
        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        
        return True
    
    for n1, n2 in edges:
        if not union(n1, n2): # adding n1, n2 together will result in a cycle
            return [n1, n2]