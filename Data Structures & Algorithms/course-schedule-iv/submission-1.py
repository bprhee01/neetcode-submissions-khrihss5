class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reqMap = defaultdict(set)
        ans = []
        for prereq, course in prerequisites:
            reqMap[course].add(prereq)

        def isPreReq(argPrereq, course):
            if argPrereq in reqMap[course]:
                return True

            seen = set()
            prereqs = deque()
            for prereq in reqMap[course]:
                prereqs.append(prereq)

            while len(prereqs):
                prereq = prereqs.pop()
                if prereq == argPrereq:
                    return True
                reqMap[course].add(prereq)
                seen.add(prereq)
                for nextPrereq in reqMap[prereq]:
                    if nextPrereq in seen:
                        continue
                    prereqs.append(nextPrereq)
            return False

        for query in queries:
            argPrereq, course = query
            ans.append(isPreReq(argPrereq, course))
        return ans