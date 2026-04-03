class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        dp = {0}
        target = stoneSum // 2


        for stone in stones:
            nextDP = set(dp)
            for curSum in dp:
                if stone + curSum == target:
                    return stoneSum - (2 * target)
                elif stone + curSum > target:
                    continue
                nextDP.add(stone + curSum)
            dp = nextDP
        print(dp)
        return stoneSum - (2 * max(dp))