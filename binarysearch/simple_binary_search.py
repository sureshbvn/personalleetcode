from typing import List

class Solution:

    # Search performs binary search on the input sorted array to search for the existence of given
    # target.
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # Note that we are using <= to cover the case of single element. Let's say the input array is
        # [5] and element to be searched is 5. If we do low<high, we will never be able to search this.
        while low <= high:

            # Calcluate mid. The formula is to avoid the integer overflow case.
            mid = low + (high - low) // 2

            # Case1:
            # The element is found in the mid. Return the index.
            if nums[mid] == target:
                return mid

            # Case 2:
            # The mid element is smaller than the target. This means that search space is to the right of the
            # mid element
            elif nums[mid] < target:
                low = mid + 1

            # Case 3:
            # The mid element is larget than the target. This means that search space is to the left of the mid
            # element.
            else:
                high = mid - 1

        # If we are here, it means the element is not present in the input array. So return -1
        return -1

# Test cases
s1 = Solution()
assert s1.search([1,2,3,4], 2) == 1
assert s1.search([1], 1) == 0
assert s1.search([1,2,3], 4) == -1
assert s1.search([-1,0,1,5,6,8,9,13,14], 5) == 3
assert s1.search([-1,0,1,5,6,8,9,13,14], -1) == 0
assert s1.search([-1,0,1,5,6,8,9,13,14], 14) == 8

