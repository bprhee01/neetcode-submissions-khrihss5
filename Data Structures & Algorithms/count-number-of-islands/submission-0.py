# [
#     ["1","1","0","0","1"]
#     ["1","1","0","0","1"]
#     ["0","0","1","0","0"]
#     ["0","0","0","1","1"]
# ]

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"

        def bfs(startR,startC):
            q = deque()
            q.append((startR,startC))
            while len(q):
                (r,c) = q.popleft()
                print("remove", r,c)
                grid[r][c] = "0"
                if isValid(r+1,c):
                    q.append((r+1,c))
                if isValid(r-1,c):
                    q.append((r-1,c))
                if isValid(r,c+1):
                    q.append((r,c+1))
                if isValid(r,c-1):
                    q.append((r,c-1))

                
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "0":
                    continue
                print(row,col)
                islands += 1
                #turn the rest into "0"
                bfs(row,col)
        return islands