class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}
        for i, num in enumerate(nums):
            if target - num not in seenNums:
                seenNums[num] = i
            else:
                return [seenNums[target-num],i]