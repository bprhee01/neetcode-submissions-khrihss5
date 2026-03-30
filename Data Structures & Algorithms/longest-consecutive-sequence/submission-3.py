class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        lowestNums = []
        lcs = 0

        #find lowest in sequence
        for num in nums:
            if num - 1 in numSet:
                continue
            else:
                lowestNums.append(num)

        for num in lowestNums:
            curr = num +1
            count = 1

            while curr in numSet:
                curr += 1
                count += 1

            if count > lcs:
                lcs = count

        return lcs