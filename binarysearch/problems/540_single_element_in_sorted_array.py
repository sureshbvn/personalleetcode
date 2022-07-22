# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
# element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.

# Boundary pattern:
# Part1: All the elements which valid pairs.
# Part2: All the elements with invalid pairs and single element.
# When the search ends, low will point to the single element

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while low <= high:
            mid = low + (high - low) // 2

            if mid % 2 == 0:
                if mid == len(nums) - 1:
                    return nums[mid]

                if nums[mid] == nums[mid + 1]:
                    low = mid + 2
                else:
                    high = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1

        return nums[low]