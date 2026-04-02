class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalWays = 0

        sums = defaultdict(int)
        sums[0] = 1
        for num in nums:
            nextSums = defaultdict(int)
            for s in sums:
                count =sums[s]
                nextSums[s + num] += count
                nextSums[s - num] += count

            sums = nextSums

        return sums[target]