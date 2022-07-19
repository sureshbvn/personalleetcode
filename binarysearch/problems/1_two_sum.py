# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create the original dictionary to keep track of indices.
        originalIdexDict = {}
        for i in range(0, len(nums)):
            originalIdexDict[nums[i]] = i

        # Sort the array so that we can do binary search.
        nums.sort()

        # Binary search helper.
        def binarySearch(start, elem):
            low = start
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == elem:
                    return mid
                elif nums[mid] < elem:
                    low = mid + 1
                else:
                    high = mid - 1

            # The element is not found.
            return -1

        # Note that window to be searched is being reduced every time.
        for i in range(0, len(nums)):
            elem = target - nums[i]
            index = binarySearch(i, elem)
            if index == -1:
                continue

            return [originalIdexDict[nums[i]], originalIdexDict[nums[index]]]

s1 = Solution()
assert s1.twoSum([2,7,11,15], 9) == [0,1]
assert s1.twoSum([3,2,4], 6) == [1,2]
assert s1.twoSum([3,1,2], 5) == [2,0]