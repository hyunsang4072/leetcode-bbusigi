# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # optimal iterative soln.
    curr = root
    stack = [] # use stack to emulate in-order traversal
    n = 0 # to keep track of how many traversals we've done so far

    while curr or stack:
        # we keep appending each node we encounter
        # until we reach null
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # in-order traversal
        node = stack.pop()
        n += 1 # don't forget to increment n each time

        # we want to return the k-th in-order traversal'd node
        # which corresponds to the k-th smalles element in BST
        # we can return here b/c we are guaranteed to find
        # the k-th smallest element
        if n == k:
            return node.val
        
        # this is b/c we also want to iterate through right children
        curr = node.right

    ####### other approach #######
    # my soln. uses recursive dfs calls to build the res list
    # res = []

    # def dfs(t):
    #     if not t: return

    #     dfs(t.left)

    #     res.append(t.val)

    #     dfs(t.right)
    
    # dfs(root)

    # return res[k - 1]