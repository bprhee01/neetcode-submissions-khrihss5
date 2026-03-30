class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        numCount = {}
        solution = []

        for num in nums:
            numCount[num] = 1 + numCount.get(num,0)
        for num in numCount:
            freq[numCount[num]].append(num)
    
        # print(freq)
        count = 0
        idx = len(nums) - 1
        while count < k:
            for num in freq[idx]:
                solution.append(num)
                count += 1
            idx -= 1
            
        return solution