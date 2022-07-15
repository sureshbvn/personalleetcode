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

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        index = 0

        # Note the eaulity case, to handle single element.
        while low <= high:
            # Case to handle integer over flow.
            mid = low + (high-low)//2

            # Case1:
            # If the current mid index value is equivalent to target, the insert position can either be current index
            # if all these elements to the left are less than the mid or the insert position can be on the left half
            # if there are more elements on the left side with same value. In case 1b, this is equivalent to finding
            # the left most index of the given element in sorted array.
            if nums[mid] == target:
                index = mid
                high = mid -1

            # Case 2:
            # The mid element is less than target, then mid index can be potential index to insert. This is the case
            # where all the elements to the right are larger than current elment at mid.
            # Another case is that is the insert position is simply on the right side and we have to move our search to
            # right
            elif nums[mid] < target:
                low = mid + 1

            # Case3:
            else:
                high = mid - 1

        return low


s1 = Solution()
print(s1.searchInsert([1],2))
#print (s1.searchInsert([1, 3, 5, 6], 5))
#print (s1.searchInsert([1,1, 3, 5, 6], 2))
#assert s1.searchInsert([1, 3, 5, 6], 5) == 2
#assert s1.searchInsert([1,1, 3, 5, 6], 2) == 2