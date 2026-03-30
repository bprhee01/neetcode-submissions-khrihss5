class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l,r =0,0

        #set initital window
        while r - l <= k and r < len(nums):
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            r += 1
        while r < len(nums):
            seen.remove(nums[l])
            l += 1
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            r += 1



        return False

