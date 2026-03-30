class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []
        numFreq = {}
        numsAtFreq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in numFreq:
                numFreq[num] = 0
            numFreq[num] += 1

        for num in numFreq:
             numsAtFreq[numFreq[num]].append(num)
            
        i = len(nums)
        kCount = 0
        while 0 <= i and kCount < k:
            for num in numsAtFreq[i]:
                topK.append(num)
                kCount += 1
            i -= 1
        print(numsAtFreq)
        return topK
