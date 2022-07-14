# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
# target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Helper method 1:
        # Get the left most index of element in a sorted array. If the element does not exist, return -1
        def getLeftMostIndexInSortedArray(arr: List[int], target) -> int:

            low = 0
            high = len(arr) - 1

            # Init to -1. If no element is found -1 can be returned.
            outputIndex = -1

            # <= to handle single element.
            while low <= high:

                mid = low + (high - low)//2

                if arr[mid] == target:
                    outputIndex = mid
                    high = mid - 1

                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return outputIndex

        # Helper method 2:
        def getRightMostIndexInSortedArray(arr: List[int], target) -> int:

            low = 0
            high = len(arr) - 1

            # Init to -1. If no element is found -1 can be returned.
            outputIndex = -1

            # <= to handle single element.
            while low <= high:

                mid = low + (high - low) // 2

                if arr[mid] == target:
                    outputIndex = mid
                    low = mid + 1

                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return outputIndex


        leftIndex = getLeftMostIndexInSortedArray(nums, target)
        if leftIndex == -1:
            return [-1, -1]

        rightIndex = getRightMostIndexInSortedArray(nums, target)
        return [leftIndex, rightIndex]

s1 = Solution()
assert s1.searchRange([1,1,1], 1) == [0,2]
assert s1.searchRange([5,7,7,8,8,10], 8) == [3,4]
assert s1.searchRange([5,7,7,8,8,10], 6) == [-1,-1]
assert s1.searchRange([], 0) == [-1,-1]




