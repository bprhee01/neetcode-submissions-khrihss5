class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        l,r = 0, 0
        freq = defaultdict(int)
        highestFreq = s[0]

        def getFreq()-> str:
            hF = highestFreq
            for k,v in freq.items():
                if v > freq[hF]:
                    hF = k
            return hF

        while r < len(s):
            freq[s[r]] += 1
            if freq[r] > freq[highestFreq]:
                highestFreq = s[r]
            while freq[highestFreq] + k < r - l + 1:
                print(l,r, freq[highestFreq] + k, r - l +1)
                freq[s[l]] -= 1
                l += 1
                highestFreq = getFreq()
            leng = r - l + 1
            kChars = leng - freq[highestFreq]
            ans = max(ans, min(len(s),leng + (k -kChars)))
            r += 1
        return ans