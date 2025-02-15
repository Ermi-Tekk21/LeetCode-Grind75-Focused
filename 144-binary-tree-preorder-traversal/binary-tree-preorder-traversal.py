from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach using a stack
        res = []
        stack = []
        cur = root
        
        while cur or stack:
            # Process the current node
            if cur:
                res.append(cur.val)  # Append the value of the current node
                stack.append(cur)    # Push the current node onto the stack
                cur = cur.left       # Move to the left child
            else:
                # Backtrack to the previous node
                cur = stack.pop()
                cur = cur.right      # Move to the right child
        
        return res