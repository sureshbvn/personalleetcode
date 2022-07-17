# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

# Example
# 1:
#
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Example
# 2:
#
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1
# Example
# 3:
#
# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums
# contains
# distinct
# values
# sorted in ascending
# order.
# -104 <= target <= 104

# The difference from (35) Search insert position is that the array can have duplicates.
# When the array has duplicates, insert at the last position the duplicate occurence instead of first occurence.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # The core logic is the following. Run the problem until the low > high. When they cross over, low will stay
        # at the position where element is first >= to target. Any element to left of this boundary will be less than
        # target and these elements cannot be disturbed. When the while loop ends, the current low pointer will contain
        # the position to add the element.
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low


s1 = Solution()
assert s1.searchInsert([1],2) == 1
assert s1.searchInsert([1, 3, 5,5,5, 6,7,7], 5) == 2