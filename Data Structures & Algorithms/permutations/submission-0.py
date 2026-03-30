class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            nextPerms = []

            for p in perms:
                for i in range(len(p)+1):
                    nP = p.copy()
                    nP.insert(i,n)
                    nextPerms.append(nP)
                perms = nextPerms
        return perms
