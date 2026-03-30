from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        topK = []

        for num in nums:
            counts[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            freq[count].append(num)
        
        for c in range(len(freq) - 1, 0, -1):
            for num in freq[c]:
                topK.append(num)
            if len(topK) == k:
                return topK


