class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for idx,num in enumerate(nums):
            target = num * -1
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                if (nums[left] + nums[right]) == target:
                    if [num,nums[left],nums[right]] not in triplets:
                        triplets.append([num,nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right]) < target:
                    left += 1
                else:
                    right -= 1
        return triplets

