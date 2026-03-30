class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def makeAnagramMap(word: str) -> str:
            map = [0] * 26
            for c in word:
                map[ord(c) - 97] += 1
            
            return str(map)
            
        
        anagrams = {}

        for word in strs:
            key = makeAnagramMap(word)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        
        return list(anagrams.values())
