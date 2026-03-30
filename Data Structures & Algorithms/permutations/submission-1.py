class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        
        for num in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    nP = p.copy()
                    nP.insert(i,num)
                    newPerms.append(nP)
            perms = newPerms
        return perms