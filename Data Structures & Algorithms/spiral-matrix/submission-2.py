class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        output = []
        while left < right and top < bottom:
            for col in range(left, right):
                output.append(matrix[top][col])
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
