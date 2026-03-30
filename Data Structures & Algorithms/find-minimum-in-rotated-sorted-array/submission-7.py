class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = (r - l) // 2
        count = 0
        while l <= r and count < 5:
            print(l,r,m)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            m = (r - l) // 2 + l
            count += 1

        return nums[m]