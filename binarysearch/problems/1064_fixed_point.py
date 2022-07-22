# Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that
# satisfies arr[i] == i. If there is no such index, return -1.

# Example
# 1:
#
# Input: arr = [-10, -5, 0, 3, 7]
# Output: 3
# Explanation: For
# the
# given
# array, arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3, thus
# the
# output is 3.
# Example
# 2:
#
# Input: arr = [0, 2, 5, 8, 17]
# Output: 0
# Explanation: arr[0] = 0, thus
# the
# output is 0.
# Example
# 3:
#
# Input: arr = [-10, -5, 3, 4, 7, 9]
# Output: -1
# Explanation: There is no
# such
# i
# that
# arr[i] == i, thus
# the
# output is -1.
#
# Constraints:
#
# 1 <= arr.length < 104
# -109 <= arr[i] <= 109
#
# Follow
# up: The
# O(n)
# solution is very
# straightforward.Can
# we
# do
# better?

# Boundary pattern.
#
# The first part contains all the elements for which nums[index] < index. We dont care about this part.
# The second part contains all the elements for which nums[indx] >= index.
# The answer will be first element of second half.

from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] < mid:
                low = mid + 1

            else:
                high = mid - 1

        if low == len(arr) or arr[low] != low:
            return -1

        return low


obj1 = Solution()
assert obj1.fixedPoint([-10, -5, -2, 0, 4, 5, 6, 7, 8, 9, 10]) == 4
assert obj1.fixedPoint([-10, -5, 0, 3, 7]) == 3
assert obj1.fixedPoint([0, 2, 5, 8, 17]) == 0
assert obj1.fixedPoint([-10, -5, 3, 4, 7, 9]) == -1