class Solution:
    def findPalindrome(self, s:str, i1: int, i2: int):
        l,r = i1,i2
        a1,a2 = i1,i2
        while 0 <= l <= r < len(s) and s[l] == s[r]:
            a1, a2 == l,r
            l -= 1
            r += 1

        return (l+1,r-1)
    def longestPalindrome(self, s: str) -> str:
        ans = (0,0)

        for i in range(len(s)):
            l1,r1 = self.findPalindrome(s,i,i)
            l2,r2 = self.findPalindrome(s,i,i+1)
            print(l1,r1,l2,r2)
            if ans[1] - ans[0] < r1 - l1:
                ans = (l1,r1)
            if ans[1] - ans[0] < r2 - l2:
                ans = (l2,r2)
        return s[ans[0]:ans[1]+1]
