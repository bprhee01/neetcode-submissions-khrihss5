class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0

        while r < len(nums):
            if r - 1 >= 0 and nums[r] == nums[r-1]:
                del nums[r]
            else:
                r += 1

        return len(nums)