class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        for i, iNum in enumerate(nums):

            if i != 0 and iNum == nums[i - 1]:
                continue
            l,r = i +1, len(nums) - 1
            comp = iNum * -1
            
            while l < r:
                lNum = nums[l]
                rNum = nums[r]
                lrSum = lNum + rNum

                if lrSum > comp:
                    r -= 1
                elif lrSum < comp:
                    l += 1
                else:
                    ans.append([iNum,lNum,rNum])
                    while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                        l += 1
                    while r - 1 >= 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        
        return ans
            