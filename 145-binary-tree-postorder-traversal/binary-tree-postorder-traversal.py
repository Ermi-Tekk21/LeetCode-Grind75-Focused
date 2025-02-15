from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach using a stack
        res = []
        stack = []
        cur = root
        last_visited = None  # To keep track of the last visited node
        
        while cur or stack:
            # Traverse to the leftmost node
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # Check the top of the stack
            top = stack[-1]
            
            # If the right subtree exists and hasn't been visited yet
            if top.right and top.right != last_visited:
                cur = top.right  # Move to the right subtree
            else:
                # Process the current node
                res.append(top.val)
                last_visited = stack.pop()  # Mark this node as visited
        
        return res