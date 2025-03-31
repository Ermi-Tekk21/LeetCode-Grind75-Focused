class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {} # dictionary to store the cloned nodes
        
        def dfs(node):
            if node in visited:
                return visited[node] # if node already visited, return the corresponding cloned node
            
            clone_node = Node(node.val, []) # create a new clone node
            
            visited[node] = clone_node # add the original node and its clone to the dictionary
            
            for neighbor in node.neighbors: # visit all the neighbors of the node
                clone_node.neighbors.append(dfs(neighbor)) # if neighbor not visited, create a new clone node and append to the neighbors list of the clone node we are currently visiting. Otherwise, append the corresponding cloned node to the neighbors list.
            
            return clone_node
        
        return dfs(node) # start DFS from the first node and return its clone
