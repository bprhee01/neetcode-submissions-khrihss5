class Solution:
    def getPalindromeCount(self, s,i1,i2):
        count = 0
        l,r = i1,i2
        while 0 <= l <= r < len(s):
            if s[l] == s[r]:
                # print(s[l],s[r],l,r)
                count += 1
                l -= 1
                r += 1
            else:
                break
        # print(count,i1,i2)
        return count
    def countSubstrings(self, s: str) -> int:
        num_palindromes = 0

        for i in range(len(s)):
            num_palindromes += self.getPalindromeCount(s,i,i)
            num_palindromes += self.getPalindromeCount(s,i,i+1)
        return num_palindromes