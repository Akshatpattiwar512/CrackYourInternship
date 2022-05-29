# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 
# 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge 
# between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

class Solution(object):
    def findRedundantConnection(self, edges):
        adjList = defaultdict(list)
        for src, dest in edges:
            adjList[src-1].append(dest-1)
            if dest-1 not in adjList:
                adjList[dest-1] = []
        # print(adjList)

        parent = [-1]*len(adjList)

        def find_parent(i):
            if parent[i] == -1:
                return i 
            else:
                return find_parent(parent[i])

        def union(x,y):
            x_set = find_parent(x)
            y_set = find_parent(y)
            parent[y_set] = x_set
            
        for edge in edges:
            src = edge[0]-1
            dest = edge[1]-1
            x = find_parent(src)
            y = find_parent(dest)
            if x == y:
                return edge
            else:
                union(x,y)
        return []
