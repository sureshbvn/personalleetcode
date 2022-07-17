# Given a characters array letters that is sorted in non-decreasing order and a character target,
# return the smallest character in the array that is larger than target.
#
# Note
# that
# the
# letters
# wrap
# around.
#
# For
# example,
# if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
#
# Example
# 1:
#
# Input: letters = ["c", "f", "j"], target = "a"
# Output: "c"
# Example
# 2:
#
# Input: letters = ["c", "f", "j"], target = "c"
# Output: "f"
# Example
# 3:
#
# Input: letters = ["c", "f", "j"], target = "d"
# Output: "f"
#
# Constraints:
#
# 2 <= letters.length <= 104
# letters[i] is a
# lowercase
# English
# letter.
# letters is sorted in non - decreasing
# order.
# letters
# contains
# at
# least
# two
# different
# characters.
# target is a
# lowercase
# English
# letter.

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        low = 0
        high = len(letters) - 1

        while low <= high:

            mid = low + (high - low) // 2
            if ord(letters[mid]) <= ord(target):
                low = mid + 1
            else:
                high = mid - 1

        low = low % len(letters)
        return letters[low]

s1 = Solution()
assert s1.nextGreatestLetter(["c", "f", "j"], "a") == "c"
assert s1.nextGreatestLetter(["c", "f", "j"], "c") == "f"
assert s1.nextGreatestLetter(["c", "f", "j"], "d") == "f"