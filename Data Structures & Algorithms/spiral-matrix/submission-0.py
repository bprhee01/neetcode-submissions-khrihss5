class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        ROWS, COLS = len(matrix), len(matrix[0])
        output = []
        nextDir = {
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }
        def getRC(r,c,dirr):
            if dirr == "right":
                return [r,c+1]
            elif dirr == "left":
                return [r,c-1]
            elif dirr == "up":
                return [r-1,c]
            elif dirr == 'down':
                return [r+1,c]
            else:
                return [r,c]

        def helper(r,c, dirr):
            print(r,c,dirr)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen:
                return False
            seen.add((r,c))
            output.append(matrix[r][c])
            #keep going same dir or turn
            [nr,nc] = getRC(r,c,dirr)
            if not helper(nr,nc,dirr):
                dirr = nextDir[dirr]
                [nr,nc] = getRC(r,c,dirr)
                return helper(nr,nc,dirr)
            return True
        helper(0,0,"right")
        return output
        