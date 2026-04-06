class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = defaultdict(list)
        preReqsLeft = [0 for _ in range(numCourses)]
        courseOrder = []
        canTake = deque()
        for course,prereq in prerequisites:
            prereqMap[prereq].append(course)
            preReqsLeft[course] += 1
        
        for course in range(numCourses):
            if preReqsLeft[course] == 0:
                canTake.append(course)

        while len(canTake):
            course = canTake.popleft()
            courseOrder.append(course)
            for nextCourse in prereqMap[course]:
                preReqsLeft[nextCourse] -= 1
                if preReqsLeft[nextCourse] == 0:
                    canTake.append(nextCourse)
        
        if len(courseOrder) == numCourses:
            return courseOrder
        else:
            return []