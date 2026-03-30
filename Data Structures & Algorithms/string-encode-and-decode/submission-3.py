class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        encoded = ""
        for s in strs:
            encoded += f"{"#"}{len(s)}{","}{s}"
        print("encoded: ", encoded)
        return encoded

    def decode(self, s: str) -> List[str]:

        def getLen(s: str, pos: int) -> (int,int):
            leng = ""
            i = pos
            
            while s[i] != ",":
                if s[i] != "#":
                    leng += s[i]
                i += 1

            return (int(leng), i + 1)


        if s == "":
            return []

        decoded = []
        pos = 0

        while pos < len(s):
            #get decoded
            lenOfStr,newPos =  getLen(s,pos)
            pos = newPos

            newS = ""
            print(lenOfStr, pos)
            while pos < newPos + lenOfStr:
                newS += s[pos]
                pos += 1

            decoded.append(newS)
            print(newS)



        return decoded
