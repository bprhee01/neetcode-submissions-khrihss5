import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        mid = l + (r - l) // 2

        while l <= r:
            cur = nums[mid]

            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
                mid = l + (r - l) // 2
            else:
                r = mid - 1
                mid = l + (r - l) // 2
        
        return -1
