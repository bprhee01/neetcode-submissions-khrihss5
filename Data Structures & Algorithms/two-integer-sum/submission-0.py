class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenValsMap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seenValsMap:
                return [seenValsMap[compliment],i]
            seenValsMap[nums[i]] = i

