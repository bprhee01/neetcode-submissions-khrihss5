#for size n
 #elements will be between 1, n-1 
 # 0 will never be a element
# 0 can act as a head
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        cycleFound = False

        while not cycleFound:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                cycleFound = True
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

        