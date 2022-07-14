#Given an array of integers nums sorted in non-decreasing order, find the ending position of a given target value.

# If target is not found in the array, return -1

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    # The function getLeftMostIndex returns the left most occurence of the target element in the sorted array.
    def getLeftMostIndex(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        # This is the output. Initialize to -1 since -1 has to returned for case the target is not found.
        outputIndex = -1

        # Note the less than equal to for single element and boundary conditions.
        while low <= high:

            # Integer overflow
            mid = low + (high-low)//2

            if nums[mid] == target:
                outputIndex = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return outputIndex

s1 = Solution()
assert s1.getLeftMostIndex([1,1,1], 1) == 0
assert s1.getLeftMostIndex([1], 1) == 0
assert s1.getLeftMostIndex([1], 0) == -1
assert s1.getLeftMostIndex([1,1,1,1,1,1,1,2,3,3,3,3], 2) == 7
assert s1.getLeftMostIndex([1,1,1,1,1,1,1,2,3,3,3,3], 3) == 8

