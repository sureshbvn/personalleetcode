# An array arr a mountain if the following properties hold:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] >
# arr[i + 1] > ... > arr[arr.length - 1].
#
# You must solve it in O(log(arr.length)) time complexity.
#
# Example
# 1:
#
# Input: arr = [0, 1, 0]
# Output: 1
# Example
# 2:
#
# Input: arr = [0, 2, 1, 0]
# Output: 1
# Example
# 3:
#
# Input: arr = [0, 10, 5, 2]
# Output: 1
#
# Constraints:
#
# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# arr is guaranteed
# to
# be
# a
# mountain
# array.

# Boundary pattern.
# Part1: All the elements for which nums[index] < nums[index+1]
# Part2: All the elements for which nums[index] > nums[index+1]
# Once the binary search is complete, low will point to the first element of Part2 which will
# be peak index. Since peak is guranteed to exist, low will not be out of bound.

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-2
        while low <= high:
                mid = low + (high - low)//2
                if arr[mid] < arr[mid+1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return low

obj = Solution()
assert obj.peakIndexInMountainArray([0, 1, 0]) == 1
assert obj.peakIndexInMountainArray([0, 2, 1, 0]) == 1
assert obj.peakIndexInMountainArray([0, 10, 5, 2]) == 1
assert obj.peakIndexInMountainArray([1]) == 0
assert obj.peakIndexInMountainArray([1,2]) == 1
assert obj.peakIndexInMountainArray([2,1]) == 0
