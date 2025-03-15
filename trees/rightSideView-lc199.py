# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    # optimal soln.
    # TC: O(n)
    # SC: O(n)
    res = []

    queue = deque([root])

    while queue:
        rightSide = None # this is necessary for edge cases
        qLen = len(queue)
        
        for i in range(qLen):
            node = queue.popleft()
            if node:
                rightSide = node
                queue.append(node.left)
                queue.append(node.right)
        
        # this has to be outside for loop!!!
        if rightSide:
            res.append(rightSide.val)
    
    return res
    
    # my soln.  <- very similar to neetcode's soln.
    # temp = []
    # res = []

    # queue = deque([root])

    # while queue:
    #     qLen = len(queue)
    #     level = []
    #     for i in range(qLen):
    #         node = queue.popleft()
    #         if node:
    #             queue.append(node.left)
    #             queue.append(node.right)
    #             level.append(node.val)
    #     if level:
    #         temp.append(level)
    
    # for l in temp:
    #     res.append(l[-1])
    
    # return res