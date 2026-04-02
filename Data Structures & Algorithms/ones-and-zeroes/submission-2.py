class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def getFreq(string):
            oneCount = 0
            zeroCount = 0
            for c in string:
                if c == "1":
                    oneCount += 1
                if c == "0":
                    zeroCount += 1
            return [zeroCount,oneCount]
       
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        strArr = []
        for string in strs:
            strArr.append(getFreq(string))

        #loop through strings already seen as freqs
        for sZeros, sOnes, in strArr:
            for zero in range(m,sZeros - 1, -1):
                for one in range(n,sOnes-1,-1):
                    dp[zero][one] = max(1+ dp[zero-sZeros][one-sOnes],dp[zero][one])
        
        return dp[m][n]