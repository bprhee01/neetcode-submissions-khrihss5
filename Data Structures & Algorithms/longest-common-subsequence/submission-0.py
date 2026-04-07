class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M,N = len(text1), len(text2)
        grid = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i+1][j+1]
                else:
                    grid[i][j] = max(grid[i][j+1], grid[i+1][j])
        return grid[0][0]