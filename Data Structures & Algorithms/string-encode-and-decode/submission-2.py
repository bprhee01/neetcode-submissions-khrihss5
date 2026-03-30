class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "saeki"
        return "saeki".join(strs)

    def decode(self, s: str) -> List[str]:
        if s =="saeki":
            return []
        return s.split("saeki")