def countComponents(self, n: int, edges: List[List[int]]) -> int:
    # TC: O(N + (E * a(N))); N = # of Nodes, E = # of Edges
    # SC: O(N)
    parent = [i for i in range(n)]
    rank = [1] * n # determines which graph gets added to which when unioning

    # find the root parent of node n
    def find(n): # O(a(N)) -> a(*) = inverse ackermann function; amortized(constant in practice)
        res = n

        while res != parent[res]:
            parent[res] = parent[parent[res]] # path compression
            res = parent[res]
        
        return res
    
    def union(n1, n2): # O(a(N)) -> a(*) = inverse ackermann function; amortized(constant in practice)
        # find parents of n1 and n2
        p1, p2 = find(n1), find(n2)

        # already in the same component
        # no need to perform union
        if p1 == p2:
            return 0

        # when unioning, determine which graph gets connected to which by checking rank arr
        # basic idea is that smaller height tree becomes the sub-tree of larger height tree's root
        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        
        return 1
    
    components = n
    for n1, n2 in edges:
        if union(n1, n2) == 1: # perform at most E operations -> O(E * a(N))
            components -= 1
    
    return components
