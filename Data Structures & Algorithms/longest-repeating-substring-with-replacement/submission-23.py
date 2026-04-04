class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l,r = 0,0
        mostFreqChar = ""
        max_length = 0
        while r < len(s):
            rC = s[r]
            freq[rC] += 1
            if freq[mostFreqChar] < freq[rC]:
                mostFreqChar = rC
            max_f = freq[mostFreqChar]
            while max_f + k < r - l + 1:
                freq[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length