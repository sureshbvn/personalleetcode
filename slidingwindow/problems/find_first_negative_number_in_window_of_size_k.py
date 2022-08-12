import collections

class Solution:
    # FirstNegativeNumbersInSubArray is a brute force solution to find the first negative number in each
    # subarray of size K.
    # The function returns a list of all the first negative numbers. If there are no negative numbers in
    # in a given subarray zero is returned.
    # Input Array = [-8, 2, 3, -6, 10]
    # Sub array size = 2
    # Potential subarrays = [-8,2], [2,3], [3,-6], [-6,10]
    # output = [-8, 0, -6, -6]. Note that in second sub array there are no negative numbers.
    # Time complexity:
    # There are (n-k) sub arrays of size k in an array of length n.
    # In each sub array there are k elements. In the brute force approach we are iterating over all the
    # elements in subarray. So in each subarray there is a work of "k".
    # Time complexity = (n-k) * k
    # Space Complexity = constant O(1)
    def FirstNegativeNumbersInSubArray(self, A, K):

        low = 0
        high = 0
        output = []

        while high < len(A):
            # If the sliding window is not formed, create the sliding window.
            while high-low+1 < K:
                high = high + 1

            # In each sub array there is a possibility there are no negative numbers. If that is the
            # case we need to catch it and append zero to the output list.
            negativeFound = False
            # At this stage we have valid sliding window.
            # Find the negative number in the sliding window.
            for i in range(low, high+1):
                if A[i] < 0:
                    output.append(A[i])
                    negativeFound = True
                    break

            # If there is no negative number in sliding window, append 0.
            if not negativeFound:
                output.append(0)

            # Move the sliding window
            low = low + 1
            high = high + 1

        return output


    # FirstNegativeNumbersInSubArrayWithDeque is an optimized version from the above.
    # In the above solution which is a brute force we exhausted all the subarrays completely to find
    # the negative element in each subarray.
    # In this we are reducing the time complexity by using some extra space.
    # The core idea is to use a deque and keep storing the negative element indices.
    # If the queue is empty, it means we have not accumlated any negative element for this subarray and we
    # append zero.
    # If the queue is non empty, the top of the queue should contain the negative number of this subarray.
    # It is important to make sure we remove the elements outside the window from the deque to make sure
    # the top of the queue always contains a relevant element for this subarray in consideration.
    # It is also important to pop off all the elements that are in this window, to keep the extra space limited
    # to O(K).
    # Time complexity: O(N)
    # Space complexity: O(K)
    # The function returns a list as output. Each element in the list is the first negative number in the subarray.
    # If there is no negative number in a subarray, we wll append zero.
    def FirstNegativeNumbersInSubArrayWithDeque(self, A, K):

        low = 0
        high = 0
        output = []
        queue = collections.deque([])

        while high < len(A):
            # If the sliding window is not formed, create the sliding window.
            while high - low + 1 < K:
                if A[high] < 0:
                    queue.append(high)
                high = high + 1

            # Now we have valid sliding window.
            if A[high] < 0:
                queue.append(high)

            # If the sliding window has indices less then low, pop them out.
            while len(queue) >0 and queue[0] < low:
                queue.popleft()

            # If the deque is empty, it means there are no negative numbers in the current subarray.
            if len(queue) == 0:
                output.append(0)
            else:
                output.append(A[queue[0]])

            low = low + 1
            high = high + 1

        return output

    # FirstNegativeNumbersInSubArraySinglePass is single pass solution without extra space
    # Time complexity: Iterate array once for sliding window. Once for potentialLastNegativeIndex.
    # 2* O(N).
    # Space : O(1)
    def FirstNegativeNumbersInSubArraySinglePass(self, A, K):

        low = 0
        high = 0
        potentialLastNegativeIndex = 0
        output = []

        while high < len(A):

            # Check if the sliding window is formed.
            while high-low+1 < K:
                high = high + 1

            # At this stage we have a valid sliding window.

            # Check potentialLastNegativeIndex is still within the sliding window and pointing to
            # a negative element. If so there is nothing to be done. We are still pointing to the first
            # negative element in the sub array.
            if potentialLastNegativeIndex >= low and A[potentialLastNegativeIndex] < 0:
                pass
            else:
               # Iterate the potentialLastNegativeIndex through out the subarray and stop at the first
               # negative element in the subarray.
               while potentialLastNegativeIndex < high:
                   potentialLastNegativeIndex = potentialLastNegativeIndex + 1
                   if A[potentialLastNegativeIndex] < 0:
                       break

            # The potential negative index can point to positive element too.
            if A[potentialLastNegativeIndex] >= 0:
                output.append(0)
            else:
                output.append(A[potentialLastNegativeIndex])

            low = low + 1
            high = high + 1
        return output


obj = Solution()
print(obj.FirstNegativeNumbersInSubArray([-8, 2, 3, -6, 10], 2))
print(obj.FirstNegativeNumbersInSubArray([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(obj.FirstNegativeNumbersInSubArray([-1,-1,-1], 2))
print(obj.FirstNegativeNumbersInSubArrayWithDeque([-8, 2, 3, -6, 10], 2))
print(obj.FirstNegativeNumbersInSubArrayWithDeque([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(obj.FirstNegativeNumbersInSubArrayWithDeque([-1,-1,-1], 2))
print(obj.FirstNegativeNumbersInSubArraySinglePass([-8, 2, 3, -6, 10], 2))
print(obj.FirstNegativeNumbersInSubArraySinglePass([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(obj.FirstNegativeNumbersInSubArraySinglePass([-1,-1,-1], 2))


