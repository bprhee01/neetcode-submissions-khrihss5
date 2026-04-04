class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, num in enumerate(nums):
            if num > 0 or i > 0 and num == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                lNum, rNum = nums[l], nums[r]
                fweeSum = num + lNum + rNum
                if fweeSum == 0:
                    ans.append([num, lNum, rNum])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif fweeSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return ans
