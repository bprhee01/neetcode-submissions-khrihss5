class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalWays = 0

        sums = defaultdict(int)
        sums[0] = 1
        for num in nums:
            nextSums = defaultdict(int)
            for s in sums:
                count =sums[s]
                for _ in range(count):
                    nextSums[s + num] += 1
                    nextSums[s - num] += 1

            sums = nextSums
            




        print(sums)
        return sums[target]