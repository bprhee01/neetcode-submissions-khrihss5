class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxL = 1
        prev = ""
        l,r = 0,1
        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                maxL = max(maxL, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                maxL = max(maxL, r - l + 1)
                r += 1
                prev = "<"
            elif arr[r-1] == arr[r]:
                r += 1
                l = r -1
                prev = ""
            else:
                l = r - 1
                prev = ""
        return maxL