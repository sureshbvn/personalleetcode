# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        low = 0
        high = 0

        maxLen = float("-INF")
        nonRepeatingSet = set()

        while high < len(s):

            # Check if the sliding window is still valid because of this new char.
            # We do this by shrinking window from left and checking if the window is valid
            # again.
            while s[high] in nonRepeatingSet:
                nonRepeatingSet.remove(s[low])
                low = low + 1

            # Add the new character in the set since we are just processing it.
            nonRepeatingSet.add(s[high])

            # At this point we have valid sliding window with non repeating characters.
            maxLen = max(maxLen, high - low + 1)

            # Move the sliding window to right.
            high = high + 1

        return maxLen

obj = Solution()
assert obj.lengthOfLongestSubstring("abcabcbb") == 3
assert obj.lengthOfLongestSubstring("bbbbb") == 1
assert obj.lengthOfLongestSubstring("pwwkew") == 3