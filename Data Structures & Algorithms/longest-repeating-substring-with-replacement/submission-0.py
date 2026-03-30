class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0,0
        maxFreq = 0
        maxLength = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq,count[s[r]])
            while (r - l + 1) - maxFreq > k:
                count[s[l]] = count.get(s[l],0) - 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1


        return maxLength

