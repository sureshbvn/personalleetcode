from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # create adj list.
        adjList = collections.defaultdict(list)
        for time in times:
            u, v, w = time
            
            # Add (v,w) here means neibhour vertex v and weight w to reach it. 
            adjList[u].append((v, w))
        
        
        # At this point adj list is created. 
        
        # Create a list which captures all the vertices. The key here is the vertex id and value is -1 if the vertex
        # is not captured and shortest distance if its captured.
        captured = [-1] * (n+1)
        
        # Initialize a priority queue needed for running Dijiktras.
        # It s a tuple of weight and vertext. The first element is weight since that is the priority.
        # Note that k is the starting vertex and we need zero network delay(cost) to reach it
        pq = [(0, k)]
        
        # Min duration variable is a tricky variable. It will maintain the delay or cost of max vertex.
        minDuration = 0 
        
        
        # Run Dijiktras as long as the priority queue is empty. 
        while len(pq) > 0:
            
            # Pop an element from priorite queue. Since priority queue can have duplicate elements, 
            # check if the element is captured if so return it.
            cost, vertex = heapq.heappop(pq)
            if captured[vertex] != -1:
                continue
            
            # If we are here the vertex is not yet captured. First capture it since this is the shortest
            # path for the vertex.
            captured[vertex] = cost
            minDuration = max(minDuration, cost)
            
            # Now lets look into neihbours of the vertex. If there is any veretx in the neighbour list,
            # that is not yet capured add the new weight to priority queue. 
            for nt in adjList[vertex]:
                neighbour, weight = nt
                if captured[neighbour] != -1:
                    continue
                
                # This can create duplicate entries for the vertex.
                heapq.heappush(pq, (cost+weight, neighbour))
            
        
        # At this this stage the priority queue is empty. So the algorithm is complete
        for i in range(1, n+1):
            if captured[i] == -1:
                return -1
            
        return minDuration

obj = Solution()
assert obj.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2