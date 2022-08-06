from typing import List

class Solution:
    def maxSubArraySum(self, arr, k):
            if len(arr) < k:
                return "Invalid"

            low = 0
            high = 0
            runningSum = 0

            unningSum = 0
            maxSum = float("-INF")

            # Iterate till the end of the array.
            while high < len(arr):

                # If the sliding window is not formed yet, simply compute the running
                # sum.
                if high - low + 1 < k:
                    runningSum = runningSum + arr[high]
                    high = high + 1
                    continue

                # At this point low points to the first element in the sliding window.
                # High points to the last element in the sliding window.

                # Add the new element to the running sum.
                runningSum = runningSum + arr[high]

                # Check if the running sum is greater than maxSum.
                if runningSum > maxSum:
                    maxSum = runningSum

                runningSum = runningSum - arr[low]
                low = low + 1
                high = high + 1

            return maxSum

obj = Solution()
#print(obj.maxSubArraySum([100, 200, 300, 400], 2))
assert obj.maxSubArraySum([100, 200, 300, 400], 2) == 700
assert obj.maxSubArraySum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39
assert obj.maxSubArraySum([2, 3], 4) == "Invalid"
