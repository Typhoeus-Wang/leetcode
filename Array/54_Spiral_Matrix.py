class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        list = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while len(list) < len(matrix[0]) * len(matrix):
            for c in range(left, right + 1):
                list.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                list.append(matrix[r][right])
            right -= 1

            if not (left <= right and top <= bottom):
                break

            for c in range(right, left - 1, -1):
                list.append(matrix[bottom][c])
            bottom -= 1

            for r in range(bottom, top - 1, -1):
                list.append(matrix[r][left])
            left += 1
        
        return list