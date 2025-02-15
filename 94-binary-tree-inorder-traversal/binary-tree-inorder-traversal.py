from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach using a stack
        res = []
        stack = []
        cur = root
        
        while cur or stack:
            # Traverse to the leftmost node
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # Process the current node
            cur = stack.pop()
            res.append(cur.val)  # Append the value, not the node
            
            # Move to the right subtree
            cur = cur.right
        
        return res