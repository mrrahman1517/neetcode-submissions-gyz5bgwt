class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        #print(left)
        right = len(matrix[0])
        #print(right)
        top = 0
        #print(top)
        bottom = len(matrix)
        #print(bottom)
        output = []
        while left < right and top < bottom:
            for col in range(left, right):
                print(top, col)
                output.append(matrix[top][col])
                print(output)
            top += 1
            for row in range(top, bottom):
                output.append(matrix[row][right - 1])
            right -= 1
            if left >= right or top >= bottom:
                break
            for col in range(right- 1, left - 1, -1):
                output.append(matrix[bottom - 1][col])
            bottom -= 1
            for row in range(bottom - 1, top - 1, -1):
                output.append(matrix[row][left])
            left += 1
        return output
