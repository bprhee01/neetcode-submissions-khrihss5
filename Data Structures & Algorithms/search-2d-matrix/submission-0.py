class Solution:
    def getCoord(self, pos, m, n):
        i = pos // n
        y = pos % n
        return (i,y)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        l = (0,0)
        r = (m - 1, n - 1)

        while (l[0] * n + l[1]) <= (r[0] * n + r[1]):
            left = l[0] * n + l[1]
            right= r[0] * n + r[1]
            mid = left + (right - left) // 2
            print(left,right,mid)
            midCoords = self.getCoord(mid,m,n)
            midAmount = matrix[midCoords[0]][midCoords[1]]
            print(midAmount, target)
            if midAmount == target:
                return True
            elif midAmount < target:
                l = self.getCoord(mid+1,m,n)
            else:
                r = self.getCoord(mid - 1,m,n)
            print(l,r)

        return False


        