# Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an
# integer k, return the kth missing number starting from the leftmost number of the array.

# Example
# 1:
#
# Input: nums = [4, 7, 9, 10], k = 1
# Output: 5
# Explanation: The
# first
# missing
# number is 5.
# Example
# 2:
#
# Input: nums = [4, 7, 9, 10], k = 3
# Output: 8
# Explanation: The
# missing
# numbers
# are[5, 6, 8, ...], hence
# the
# third
# missing
# number is 8.
# Example
# 3:
#
# Input: nums = [1, 2, 4], k = 3
# Output: 6
# Explanation: The
# missing
# numbers
# are[3, 5, 6, 7, ...], hence
# the
# third
# missing
# number is 6.
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 107
# nums is sorted in ascending
# order, and all
# the
# elements
# are
# unique.
# 1 <= k <= 108
#
# Follow
# up: Can
# you
# find
# a
# logarithmic
# time
# complexity(i.e., O(log(n)))
# solution?

# Boundary Pattern
# First group represents the fact that total number of missing elements is less than k
# Second group represents the fact the total number of missing elements are greater than equal to k.
# Once the while loop ends, high points to the last element of the group.
# The kth missing element will be nums[high] + (num missing elements so far - k)

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Missing elements can be found by subtracting the current element in the array and
            # expected value in the array. If the delta is zero there are no missing elements
            numMissingElements = nums[mid] - (nums[0] + mid)

            if numMissingElements < k:
                low = mid + 1
            else:
                high = mid - 1

        # When the iteration ends, high points to last element in first group.
        # Start points to the first element in second group.
        missingSoFar = nums[high] - (nums[0] + high)
        return nums[high] + (k - missingSoFar)


obj = Solution()
assert obj.missingElement([4,7,9,10],1) == 5
assert obj.missingElement([4,7,9,10],3) == 8
assert obj.missingElement([1,2,4],3) == 6