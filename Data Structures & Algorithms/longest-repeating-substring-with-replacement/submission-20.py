class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        longest = 0
        maxf = 0
        l,r = 0,0

        while r < len(s):
            freq[s[r]] += 1
            maxf = max(freq.values())

            while maxf + k < r - l + 1:
                freq[s[l]] -= 1
                l += 1
                # maxf = max(freq.values())
            longest = max(longest, r - l + 1)
            r += 1

        return longest
