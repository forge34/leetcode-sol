from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        xbl1, ybl1, xtr1, ytr1 = rec1
        xbl2, ybl2, xtr2, ytr2 = rec2

        startx = max(xbl1, xbl2)
        endx = min(xtr1, xtr2)

        starty = max(ybl1, ybl2)
        endy = min(ytr1, ytr2)

        width = endx - startx
        height = endy - starty

        return width > 0 and height > 0


sol = Solution()

print(sol.isRectangleOverlap([0,0,2,2],[1,1,3,3]))




