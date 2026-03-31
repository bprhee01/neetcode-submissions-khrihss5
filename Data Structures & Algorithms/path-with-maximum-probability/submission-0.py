class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probMap = defaultdict(list)
        for i in range(len(edges)):
            a,b = edges[i]
            probMap[a].append((succProb[i],b))
            probMap[b].append((succProb[i],a))
        
        maxheap = []
        heapq.heappush(maxheap, (-1, start_node))
        visited = set()
        while len(maxheap):
            probability, node = heapq.heappop(maxheap)
            if node in visited:
                continue
            if node == end_node:
                return -probability
            visited.add(node)

            for probN, neighbor in probMap[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(maxheap,(probability * probN, neighbor))
        return 0