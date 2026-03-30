class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1
        m = (l +r) // 2

        while l <= r:
            if nums[m] == target:
                return m

            if nums[m] > nums[r]: # left side is sorted:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # right side is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            m = (l+r) // 2

        return -1