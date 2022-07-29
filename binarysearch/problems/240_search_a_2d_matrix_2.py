# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Example
# 1:
#
# Input: matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
#                  [18, 21, 23, 26, 30]], target = 5
# Output: true
# Example
# 2:
#
# Input: matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
#                  [18, 21, 23, 26, 30]], target = 20
# Output: false
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All
# the
# integers in each
# row
# are
# sorted in ascending
# order.
# All
# the
# integers in each
# column
# are
# sorted in ascending
# order.
# -109 <= target <= 109


# Start with right most corner element.
# If the element is equal return True
# If the element is less than target, move down (i=i+1)
# If the element is more than target, move left(j=j-1)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        numrows = len(matrix)
        numcols = len(matrix[0])

        i = 0
        j = numcols - 1

        while i >= 0 and i < numrows and j >= 0 and j < numcols:

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j = j - 1
            else:
                i = i + 1

        return False

obj = Solution()
assert  obj.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5) == True
assert  obj.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20) == False