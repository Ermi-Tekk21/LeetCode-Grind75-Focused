"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        def bfs(q):
            while q:
                #Populate the next pointer
                for i in range(len(q)-1):
                    q[i].next = q[i+1]
                #Iterate through q -- Add all children
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        q = collections.deque()
        q.append(root)
        bfs(q)
        
        return root