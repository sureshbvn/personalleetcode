# In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
#
# A value from arr was removed that was not the first or last value in the array.
#
# Given arr, return the removed value.

# Example
# 1:
#
# Input: arr = [5, 7, 11, 13]
# Output: 9
# Explanation: The
# previous
# array
# was[5, 7, 9, 11, 13].
# Example
# 2:
#
# Input: arr = [15, 13, 12]
# Output: 14
# Explanation: The
# previous
# array
# was[15, 14, 13, 12].
#
# Constraints:
#
# 3 <= arr.length <= 1000
# 0 <= arr[i] <= 105
# The
# given
# array is guaranteed
# to
# be
# a
# valid
# array.

# Compute d = (lastelement-firstelement)/(len of array)
# Boundary Pattern:
# Part1: All the elements which are in right sequence. This can be found out by
# arr[index] == arr[0] + (d * index)
# Part2: All the other elements
# when the binary search finishes, the high points to last element in first group
# and low points to first element in second group
# The answer is nums[high] + d


from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        arr.sort()

        d = (arr[len(arr) - 1] - arr[0]) // (len(arr))

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == (arr[0] + d * mid):
                low = mid + 1
            else:
                high = mid - 1

        # Once the while loop is done, start will point to first bad element
        # end will point to last good element
        # so the missing element will be nums[high] + d
        return arr[high] + d

obj = Solution()
assert  obj.missingNumber([5,7,11,13]) == 9
assert  obj.missingNumber([15,13,12]) == 14