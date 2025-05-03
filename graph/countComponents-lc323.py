def countComponents(self, n: int, edges: List[List[int]]) -> int:
    parent = [i for i in range(n)]
    rank = [1] * n # determines which graph gets added to which when unioning

    # find the root parent of node n
    def find(n):
        res = n

        while res != parent[res]:
            parent[res] = parent[parent[res]]
            res = parent[res]
        
        return res
    
    def union(n1, n2):
        # find parents of n1 and n2
        p1, p2 = find(n1), find(n2)

        # already in the same component
        # no need to perform union
        if p1 == p2:
            return 0

        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        
        return 1
    
    components = n
    for n1, n2 in edges:
        if union(n1, n2) == 1:
            components -= 1
    
    return components
