class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        groupFreqDict = [set() for i in range(len(nums))]
        largestFreq = 0 
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
                groupFreqDict[0].add(num)
            else:
                freqMap[num] += 1
                groupFreqDict[freqMap[num]-2].remove(num)
                groupFreqDict[freqMap[num]-1].add(num)

                largestFreq = max(largestFreq,freqMap[num]-1)

        answer = []
        i = largestFreq
        while len(answer) < k:
            for num in groupFreqDict[i]:
                answer.append(num)
            i -= 1


        return answer
