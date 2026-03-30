
class Solution:

    def getAnagram(self,string: str) -> str:
        anagram = [0] * 26
        for c in string:
            anagram[ord(c) - 97] += 1
        # print(anagram)
        return str(anagram)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupsOfAnagrams = {}
        for string in strs:
            anagram = self.getAnagram(string)
            # print(anagram)
            if anagram in groupsOfAnagrams:
                groupsOfAnagrams[anagram].append(string)
            else:
                groupsOfAnagrams[anagram] = [string]
        return groupsOfAnagrams.values()

