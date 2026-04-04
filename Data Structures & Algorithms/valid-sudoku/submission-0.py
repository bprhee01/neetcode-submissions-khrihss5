class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def getBoxNum(r,c0):
            return(r // 3) * 3 + (c // 3)
        colDict = defaultdict(set)
        rowDict =defaultdict(set) #at row[key] the value is all seen nums in that row
        boxDict = defaultdict(set)


        for r in range(9):
            for c in range(9):
                num = board[c][r]
                if num == ".":
                    continue
                if num in colDict[c] or num in rowDict[r] or num in boxDict[getBoxNum(r,c)]:
                    return False
                colDict[c].add(num)
                rowDict[r].add(num)
                boxDict[getBoxNum(r,c)].add(num)
    
        return True