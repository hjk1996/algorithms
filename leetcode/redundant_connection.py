# tag: union find, graph
# description
'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # parent array
        par = [i for i in range(len(edges)+1)]
        # rank array
        # rank means the number of nodes in the subtree including the node itself
        rank = [1 for i in range(len(edges)+1)]
        
        # find the root of node n
        def find(n):
            # n == par[n] means that node n is a root 
            if n != par[n]:
                return find(par[n])
            return n
        
        # merge two nodes
        def union(n1, n2):
            # find the root of n1 and n2
            p1, p2 = find(n1), find(n2)
            # if root is the same, it means there is a cycle
            # because n1 and n2 are already connected by the same root
            # so, return False
            if p1 == p2:
                return False
            
            # merge two nodes
            # merge the node with smaller rank to the node with larger rank
            # because the node with larger rank has more nodes in its subtree
            # so, the node with larger rank should be the parent of the node with smaller rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            # if union(n1, n2) returns False, it means there is a cycle
            if not union(n1, n2):
                # so, return [n1, n2]
                return [n1, n2]
                