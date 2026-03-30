class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            # print(i, board[r][c])
            if i == len(word):
                return True
            if r  < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in path or board[r][c] != word[i]:
                return False
            print("never")
            path.add((r,c))
            if dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1):
                return True
            path.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False