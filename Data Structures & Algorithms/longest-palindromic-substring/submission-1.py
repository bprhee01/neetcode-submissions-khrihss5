class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_length_palindrome(l,r):
            length = (l,r)
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l+1,r-1)

        l,r = 0,0
        for i in range(len(s)):
            (l1,r1) = get_length_palindrome(i,i+1)
            (l2,r2) = get_length_palindrome(i,i)
            print(l1,r1, "second: ", l2,r2)
            if r - l + 1 < r1 - l1 + 1:
                l, r  = l1, r1
            if r - l + 1 < r2 - l2 + 1:
                l, r = l2, r2
        
        print(l,r)
        return s[l:r+1]