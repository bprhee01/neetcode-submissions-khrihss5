class Solution:
    def getCharMap(self,string):
        charMap = [0 for i in range(26)]
        # print(charMap)
        for char in string:
            charMap[ord(char) - 97] += 1
        return str(charMap)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            charMap = self.getCharMap(string)
            if charMap not in groups:
                groups[charMap] = []
            groups[charMap].append(string)

        return groups.values()
