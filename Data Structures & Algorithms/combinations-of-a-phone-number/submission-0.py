class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        combos = [""]
        for digit in digits:
            print(mapping[digit])
            nextCombo = []
            for combo in combos:
                for char in mapping[digit]:
                    print("char",char)
                    cP = combo + char
                    # cP += char
                    nextCombo.append(cP)
            combos = nextCombo

        return combos