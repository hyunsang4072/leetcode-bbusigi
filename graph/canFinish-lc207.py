def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # make a graph that follows the prerequisites
    # if cycle, return False
    # otherwise, return True
    courses = defaultdict(list)
    visited = set()

    # pre-processing
    for c, p in prerequisites:
        courses[c].append(p)

    def dfs(c): # c = course
        # TODO: 2 base cases
        if c in visited:
            return False
        if not courses[c]: # if empty list -> can finish
            return True
        
        visited.add(c)

        for pre in courses[c]: # {c: [p1, ..., pn]}
            if not dfs(pre):
                return False
        
        # clean the visited set
        # we want to avoid cycles, not revisiting
        # the same node multiple times
        visited.remove(c)
        courses[c] = []

        return True
    
    # this is due to the possibility of having
    # disconnected graphs
    for i in range(numCourses):
        if not dfs(i):
            return False

    return True