# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that
# there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.

from typing import List
import collections
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Create adj list that is empty. Note that we are using default dict.
        # This assumes an empty list during the append. This avoids additional
        # checks for us to check if the element is in the map and do an
        # initilization to empty list.
        adjList = defaultdict(list)

        for edge in edges:
            src, dest = edge
            adjList[src].append(dest)
            adjList[dest].append(src)

        # bfs is an inner function. It perform the bfs traversal on the graph starting the source
        # vertex and returns once the traversal is complete.
        # Input: source vertex to start bfs from. Global visited set to count connected components.
        # Output: None
        def bfs(source, visited):
            queue = collections.deque([source])

            while len(queue) > 0:
                vertex = queue.popleft()

                for neighbor in adjList[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        # dfs is an inner function. It performs dfs traversal on the graph.
        # Input: Source vertex to start dfs
        def dfs(source, visited):

            for neighbor in adjList[source]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited)

        # Global visisted set.
        visited = set()
        connected = 0

        # For each vertex in the graph do a BFS. When the BFS is started from a given vertex, it will
        # not complete until all the vertices are covered.
        # Every time BFS ends, we finished one connected component.
        for vertex in range(0, n):
            if vertex not in visited:
                #bfs(vertex, visited)
                dfs(vertex,visited)
                connected = connected + 1

        return connected

solution = Solution()
assert (solution.countComponents(5, [[0,1],[1,2],[3,4]]) == 2)
assert (solution.countComponents(5, [[0,1],[1,2],[2,3], [3,4]]) == 1)
assert (solution.countComponents(5, [[0,1],[3,4]]) == 3)
assert (solution.countComponents(2, [[0,1]]) == 1)
assert (solution.countComponents(2, []) == 2)

# cycle case
assert (solution.countComponents(5, [[0,1],[1,2],[2,3], [3,4], [4,1]]) == 1)