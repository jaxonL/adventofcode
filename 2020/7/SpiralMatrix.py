"""
Dec 7 LeetCode challenge (https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/)

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""

class SpiralMatrix(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.__genMatrixHelper(n)
    
    def __genMatrixHelper(self, n, offset=0):
        if n is 1:
            return [[1 + offset]]
        if n is 2:
            return [[1 + offset, 2 + offset], [4 + offset, 3 + offset]]
        
        # n >= 3
        # 1 => n
        firstRow = [x for x in range(1 + offset, n+1 + offset)]
        # n + 2(n-1) => 2n - 1
        lastRow = [x for x in range(n + 2 * (n - 1) + offset, 2*n - 2 + offset, -1)]

        leftOffset = 4* (n - 1) + offset
        # print('first:', firstRow, 'last:', lastRow, 'new offset:', leftOffset, '(', offset, ')')
        centreMatrix = self.__genMatrixHelper(n-2, leftOffset)
        # print('centreMatrix:', centreMatrix)
        rightOffset = n + 1 + offset
        for centreRow in centreMatrix:
            centreRow.insert(0, leftOffset)
            centreRow.append(rightOffset)
            leftOffset -= 1
            rightOffset += 1
        # print('new centreMatrix', centreMatrix)
        centreMatrix.insert(0, firstRow)
        centreMatrix.append(lastRow)
        return centreMatrix

def prettyPrintMatrix(spiral):
    print('Spiral Matrix for', len(spiral))
    for x in spiral:
        print('\t', x)
    print('\n')
    

prettyPrintMatrix(SpiralMatrix().generateMatrix(3))
prettyPrintMatrix(SpiralMatrix().generateMatrix(4))
prettyPrintMatrix(SpiralMatrix().generateMatrix(7))
