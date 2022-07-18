# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Example
# 1:
#
# Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
# Output: true
# Example
# 2:
#
# Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
# Output: false
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = (len(matrix) * len(matrix[0])) - 1

        # Helper function to convert 1D index to 2D index.
        def get2DIndex(index) -> List[int]:
            nc = len(matrix[0])
            return [index // nc, index % nc]

        while low <= high:
            mid = low + (high - low) // 2

            r, c = get2DIndex(mid)

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
