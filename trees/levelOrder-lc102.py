# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # Iterative BFS approach
    # TC: O(n)
    # SC: O(n)
    res = [] # outer list

    if not root: return res

    queue = deque([root])

    while queue:
        qLen = len(queue)
        level = [] # inner list
        for i in range(qLen): # to get all nodes(except null) at same level(depth)
            node = queue.popleft()
            if node: # takes care of null nodes
                queue.append(node.left)
                queue.append(node.right)
                level.append(node.val)
        if level: # we could potentially have empty list
            res.append(level)
    
    return res