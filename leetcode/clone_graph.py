# tag: graph, dfs. hashtable
# description
'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

'''

# dfs solution
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # if node is None, just return None
        if not node:
            return None


        hashMap = {}

        def dfs(node):
            # base case
            # if node is already cloned, return the clone
            if node in hashMap:
                return hashMap[node]
    
            # recursive case
            # clone the node
            clone = Node(val=node.val)
            # map the node to the clone
            hashMap[node] = clone
            # clone all neighbors recursively
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            
            return clone

        return dfs(node)
                

