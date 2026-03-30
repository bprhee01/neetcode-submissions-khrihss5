class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjMap = []
        output = {}

        for i in range(n):
            adjMap.append([])
            output[i] = -1
        for source, dest, weight in edges:
            adjMap[source].append((dest,weight))
        
        minHeap = [(0,src)]

        while minHeap:
            (weight, node) = heapq.heappop(minHeap)
            if output[node] != -1:
                continue
            output[node] = weight
            for adjNode,adjWeight in adjMap[node]:
                if output[adjNode] == -1:
                    heapq.heappush(minHeap, (weight + adjWeight, adjNode))

        return output
