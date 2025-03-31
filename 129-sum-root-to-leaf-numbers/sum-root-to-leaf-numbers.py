# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode] , val = 0) -> int:
        if not root:
            return 0
        q = [root]
        sum = 0
        while(q):
            node  = q.pop()
            if not node.left and not node.right:
                sum+=node.val
            
            if node.left:
                node.left.val += node.val*10
                q.append(node.left)
            if node.right:
                node.right.val += node.val*10
                q.append(node.right)
        return sum




class Solution:
    def sumNumbers(self, root: Optional[TreeNode] , val = 0) -> int:
        if not root:
            return 0
        q = [(root , str(root.val))]
        sum = 0
        while(q):
            node ,val = q.pop()
            if not node.left and not node.right:
                sum+=int(val)
            if node.left:
                q.append((node.left , val + str(node.left.val)))
            if node.right:
                q.append((node.right , val + str(node.right.val)))
        return sum





class Solution:
    def sumNumbers(self, root: Optional[TreeNode] , val = 0) -> int:
        if not root:
            return 0
        val = 10 * val + root.val
        if not root.left and not root.right:
            return val

        return self.sumNumbers(root.left , val) + self.sumNumbers(root.right , val)