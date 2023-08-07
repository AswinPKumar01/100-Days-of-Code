class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = bisect_left(matrix, target, key=lambda row: row[-1])
        return r < len(matrix) and matrix[r][bisect_left(matrix[r], target)] == target
