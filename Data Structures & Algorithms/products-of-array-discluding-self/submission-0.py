class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCounter = 0
        output = [0 for x in range(len(nums))]
        runningTotal = 1

        for num in nums:
            if num == 0:
                zeroCounter += 1
            else:
                runningTotal *= num

    

        if zeroCounter > 1:
            return output
        
        if zeroCounter == 1:
            for idx in range(len(nums)):
                print(nums[idx])
                if nums[idx] == 0:
                    output[idx] = runningTotal
                    return output
        
        for idx in range(len(nums)):
            output[idx] = runningTotal // nums[idx]

        return output
        

        

        