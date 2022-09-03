from typing import List
import collections
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Step1: Construct the adj list.
        adjList = defaultdict(list)
        
        for edge in edges:
            u,v = edge
            
            adjList[u].append(v)
            
            # Undirected graph. Add in both the lists
            adjList[v].append(u)
            
        
        # Step2(a). Write an inner function called bfs. This is an iterative function.
        # The function returns a boolean to indicate if a cycle is found.
        def bfs(source, visitedSet) -> bool:
            
            queue = collections.deque([source])
            visitedSet.add(source)
            parentMap = {}
            
            while len(queue) > 0:
                node = queue.popleft()
                
                for vertex in adjList[node]:
                    if vertex not in visitedSet:
                        parentMap[vertex] = node
                        visitedSet.add(vertex)
                        queue.append(vertex)
                    else:
                        # If we are seeing a node that is already visited. There are two cases. Either the node could be the parent(because its undirected graph). If so its not a cycle. The other case is the edge is a cross edge. Backedges are not possible in BFS.
                        if parentMap[node] != vertex:
                            return True
            return False
        
        
        # Step 2(b)
        # Dfs on the graph. Returns true if there is cycle. 
        def dfs(source, parent, visitedSet) -> bool :
            
            for vertex in adjList[source]:
                if vertex not in visitedSet:
                    visitedSet.add(vertex)
                    if dfs(vertex, source, visitedSet):
                        return True         
                else:
                    if vertex != parent:
                        return True
            
            return False
                        
        
        # Step3: The actual logic.
        visitedSet = set()
        connected = 0
        for node in range(0, n):
            if node not in visitedSet:
                # If atleast one connected component returns cycle, return true.
                #if bfs(node, visitedSet):
                    #return False
                    
                # In case of dfs add the node to visited. We can do this for BFS too.
                visitedSet.add(node)
                
                # With DFS we can just send parent to the recursion. This avoids have a parent Map that
                # we had in BFS iterative solution. 
                if dfs(node, None, visitedSet):
                    return False
                
                # The number of connected components should be strictly one for the graph to be a valid tree.
                connected +=1 
                if connected > 1:
                    return False
        
        # If we reach here the graph is a valid tree.
        return True

obj = Solution()
assert obj.validTree(5,[[0,1],[0,2],[0,3],[1,4]]) == True
assert obj.validTree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]]) == False