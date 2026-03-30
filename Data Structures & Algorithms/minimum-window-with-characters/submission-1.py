class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortestRange = (0,len(s)+1)
        l,r = 0,0
        tMap = {}
        sMap = {}

        def isSubstring():
            for c in tMap:
                if tMap[c] > sMap.get(c,0):
                    return False
            return True
        def getSS():
            i,j = shortestRange
            answer = ""
            while i <= j:
                answer += s[i]
                i +=1
            return answer
        for c in t:
            tMap[c] = 1 + tMap.get(c,0)
        
        while r < len(s):
            sMap[s[r]] = 1 + sMap.get(s[r],0)
            
            while isSubstring():
                print(sMap)
                if s[l] in tMap and sMap[s[l]] == tMap[s[l]]:
                    break
                sMap[s[l]] -= 1
                l += 1

            if isSubstring() and (shortestRange[1] - shortestRange[0]) > r - l:
                print(l,r)
                shortestRange = (l,r)
            r += 1


        # print(shortestRange[1] == len(s) + 1)
        if shortestRange[1] == len(s) + 1:
            return ""
        return getSS()
            