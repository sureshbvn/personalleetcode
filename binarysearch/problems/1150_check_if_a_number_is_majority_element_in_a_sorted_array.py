# Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.
#
# A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

# Example
# 1:
#
# Input: nums = [2, 4, 5, 5, 5, 5, 5, 6, 6], target = 5
# Output: true
# Explanation: The
# value
# 5
# appears
# 5
# times and the
# length
# of
# the
# array is 9.
# Thus, 5 is a
# majority
# element
# because
# 5 > 9 / 2 is true.
# Example
# 2:
#
# Input: nums = [10, 100, 101, 101], target = 101
# Output: false
# Explanation: The
# value
# 101
# appears
# 2
# times and the
# length
# of
# the
# array is 4.
# Thus, 101 is not a
# majority
# element
# because
# 2 > 4 / 2 is false.
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i], target <= 109
# nums is sorted in non - decreasing
# order.

from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        def getBoundaryOccurenceIndex(nums: List[int], elem: int, isLeftMost: bool) -> int:

            low = 0
            high = len(nums) - 1

            outputIndex = -1
            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == elem:
                    outputIndex = mid
                    if isLeftMost:
                        high = mid - 1
                    else:
                        low = mid + 1

                elif nums[mid] < elem:
                    low = mid + 1
                else:
                    high = mid - 1

            return outputIndex

        # Compute the left most index of target element. If it is -1, it means the element does not exist in the array
        # and it cannot be majority element.
        leftIndex = getBoundaryOccurenceIndex(nums, target, True)

        # Element does not exist.
        if leftIndex == -1:
            return False

        # If we are here comput the right most index of the element.
        rightIndex = getBoundaryOccurenceIndex(nums, target, False)

        # The length of window of this element should be greater than nums.length/2 for the element to be majority
        # element.
        if (rightIndex - leftIndex + 1) > len(nums) // 2:
            return True
        else:
            return False