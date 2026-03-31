class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #times hold place1,place2,time
        #n is how many places
        #k is starting node
        adjMap = defaultdict(list)
        for n1,n2,time in times:
            adjMap[n1].append((n2,time))


        delayTimes = {}
        maxTime = 0

        minheap = []
        heapq.heappush(minheap,(0,k))

        while len(minheap):
            time, node = heapq.heappop(minheap)
            if node in delayTimes:
                continue
            delayTimes[node] = time
            maxTime = max(maxTime,time)
            for (neighbor,tNeighbor) in adjMap[node]:
                if neighbor in delayTimes:
                    continue
                heapq.heappush(minheap,(time+tNeighbor, neighbor))
                
        if len(delayTimes) != n:
            maxTime = -1
        return maxTime