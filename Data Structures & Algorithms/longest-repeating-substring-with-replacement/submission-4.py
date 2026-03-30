class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls = 0
        l = 0
        freqChart = {}
        mostFreq = s[0]

        for r in range(len(s)):
            freqChart[s[r]] = freqChart.get(s[r],0) + 1
            if freqChart[mostFreq] < freqChart[s[r]]:
                mostFreq = s[r]
            mostFreqThisTime = freqChart[mostFreq]
            while (r - l + 1 - mostFreqThisTime) > k:
                freqChart[s[l]] -= 1
                l += 1
            print(l,r)
            ls = max(ls, r - l + 1)
        
        return ls