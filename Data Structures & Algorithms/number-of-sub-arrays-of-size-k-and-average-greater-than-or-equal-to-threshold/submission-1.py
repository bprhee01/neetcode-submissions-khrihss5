class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        l,r = 0,0
        sum = 0

        while r < len(arr):
            sum += arr[r]
            print(l,r, sum)
            if r - l + 1 == k and sum / k >= threshold:
                ans += 1
            if r - l + 1 == k:
                sum -= arr[l]
                l += 1
            r += 1
        return ans
            
        