class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqMap = defaultdict(list)
        preReqCount = [0 for _ in range(numCourses)]
        for course,prereq in prerequisites:
            reqMap[prereq].append(course)
            preReqCount[course] += 1
        
        preReqsTaken = deque()
        for course in range(len(preReqCount)):
            if preReqCount[course] == 0:
                preReqsTaken.append(course)
        
        completedCourses = 0
        print(preReqsTaken)
        while len(preReqsTaken):
            course = preReqsTaken.popleft()
            print(course)
            completedCourses += 1
            for unlockedCourse in reqMap[course]:
                preReqCount[unlockedCourse] -= 1
                if preReqCount[unlockedCourse] == 0:
                    preReqsTaken.append(unlockedCourse)
        print(preReqCount)
        return completedCourses == numCourses