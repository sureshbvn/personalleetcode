# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example
# 1:
#
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call
# isBadVersion(3) -> false
# call
# isBadVersion(5) -> true
# call
# isBadVersion(4) -> true
# Then
# 4 is the
# first
# bad
# version.
# Example
# 2:
#
# Input: n = 1, bad = 1
# Output: 1
#
# Constraints:
#
# 1 <= bad <= n <= 2^31 - 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    badVersion = 0

    def setBadVersion(self, bad):
        self.badVersion = bad


    def firstBadVersion(self, n: int) -> int:

        def isBadVersion(b):
            if b >= self.badVersion:
                return True
            else:
                return False

        low = 0
        high = n - 1

        # This is the output number to return. The minimum number of bad value is 1.
        output = 1
        while low <= high:
            mid = low + (high - low) // 2

            if isBadVersion(mid + 1):
                # The actual number is one greater than the index.
                output = mid + 1
                high = mid - 1
            else:
                low = mid + 1

        return output

s1 = Solution()

s1.setBadVersion(32)
assert  s1.firstBadVersion(100) == 32


s1.setBadVersion(1)
assert  s1.firstBadVersion(1) == 1

s1.setBadVersion(4)
assert  s1.firstBadVersion(5) == 4