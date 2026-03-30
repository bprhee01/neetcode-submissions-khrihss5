class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIdx = None
        products = []
        total = 1

        for i, num in enumerate(nums):
            if num == 0 and zeroIdx == None:
                print('here')
                products = [0 for _ in range(len(nums))]
                zeroIdx = i
                continue
            elif num == 0:
                return products
            total *= num
        
        if zeroIdx:
            products[zeroIdx] = total
            return products
        #for normal cases
        for num in nums:
            products.append(total // num)

        return products