class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ans = ""
        
        #get mapping of t
        tFreq = {}
        for char in t:
            tFreq[char] = tFreq.get(char,0) + 1
        
        [l,r] = 0,0
        cFreq = defaultdict(int)
        cValid = set()
        while r < len(s):
            cR = s[r]
            cFreq[cR] += 1
            if tFreq.get(cR) and tFreq[cR] <= cFreq[cR]:
                cValid.add(cR)

            #case where valid substr
            if len(cValid) == len(tFreq):
                while l <= r:
                    if ans == "" or len(ans) > r -l + 1:
                        ans = s[l:r+1]
                    cL = s[l]
                    cFreq[cL] -= 1
                    l += 1
                    if tFreq.get(cL) and tFreq[cL] > cFreq[cL]:
                        cValid.remove(cL)
                        break
            r += 1

        return ans
