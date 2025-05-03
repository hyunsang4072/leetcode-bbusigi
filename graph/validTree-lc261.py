def validTree(self, n: int, edges: List[List[int]]) -> bool:
    visited = set()
    # generate adjacency list
    adj = defaultdict(list)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1) # undirected graph
    
    # check1: #Nodes = #Edges + 1 <- Tree property
    if n != len(edges) + 1:
        return False # not a Tree
    
    # check2: are all nodes connected == is our graph a connected graph?
    def dfs(i, prev):
        if i in visited:
            return False
        
        visited.add(i)

        for nei in adj[i]:
            if nei == prev:
                continue
            if not dfs(nei, i): # current node i becomes prev for node nei
                return False
        
        return True
    
    # use -1 for base case since
    # -1 is never visited == -1 will never be prev node of any nodes
    return dfs(0, -1) and len(visited) == n
    