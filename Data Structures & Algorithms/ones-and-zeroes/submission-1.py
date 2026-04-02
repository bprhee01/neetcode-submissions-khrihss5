class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # m refers to 1 capactiy
        # n refers to 0 capacity
        #if i can record 1 by 1, choosing to skip, holding current 1s and 0s

        def get10s(string):
            c1,c2 = 0,0
            for c in string:
                if c == "1":
                    c1 += 1
                if c == "0":
                    c2 += 1
            return (c1,c2)

        maxForm = 0
        subsets = set() # will be a tuple full of (count, 1count, 0 count)
        subsets.add((0,0,0))

        for string in strs:
            nextSubsets = subsets.copy()

            (stringOneCount,stringZeroCount) = get10s(string)

            for (count,oneCount,zeroCount) in subsets:
                newOneCount, newZeroCount = oneCount + stringOneCount, zeroCount + stringZeroCount
                if newOneCount > n or newZeroCount > m:
                    continue
                nextSubsets.add((count + 1, newOneCount,newZeroCount))
                # print(count+1, newOneCount,newZeroCount)
                maxForm = max(maxForm, count + 1)
            subsets = nextSubsets
        return maxForm
            

