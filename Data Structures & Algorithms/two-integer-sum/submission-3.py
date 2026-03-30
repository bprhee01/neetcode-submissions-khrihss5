class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compDict = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in compDict:
                return [compDict[comp],i]
            else:
                compDict[num]= i