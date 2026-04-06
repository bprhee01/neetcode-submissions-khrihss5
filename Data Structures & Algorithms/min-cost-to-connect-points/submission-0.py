class Solution:
    def getCost(self, point1,point2):
        x1,y1 = point1
        x2,y2 = point2
        return abs(x1-x2) + abs(y1-y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        totalCost = 0
        visitedPoints = set()
        minHeap = [(0,(points[0][0], points[0][1]))]

        unvisitedPoints = set()
        for x,y in points:
            unvisitedPoints.add((x,y))

        while len(visitedPoints) < len(points) and len(minHeap):
            cost, curPoint = heapq.heappop(minHeap)
            if curPoint in visitedPoints:
                continue
            totalCost += cost
            visitedPoints.add(curPoint)
            unvisitedPoints.remove(curPoint)

            for otherPoint in unvisitedPoints:
                heapq.heappush(minHeap, (self.getCost(curPoint,otherPoint), otherPoint))
            
        return totalCost

