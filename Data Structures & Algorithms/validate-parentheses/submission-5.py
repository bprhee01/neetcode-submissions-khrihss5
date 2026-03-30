class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        table = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for c in s:
            if c in table:
                q.append(c)
            else: 
                if not len(q) or table[q.pop()] != c:
                    return False
        
        if len(q):
            return False
        return True
                
