# Given a monotonically increasing function f(x) on positive numbers, find the value of x when f(x) becomes positive for
# the first time. In other words, find a positive number x such that f(x-1), f(x-2), … are negative and f(x+1),
# f(x+2), … are positive.

class Solution:

    def firstPositiveNumber(self, equation: str) -> int:

        # The equation is in the format of x.
        def getEqVal(equation, x) -> int:
            return eval(equation)


        # expoSearch runs an exponential search in the range starting (0, INF)
        # The search range is divided into
        # 2^0- 2^1
        # 2^1- 2^2
        # 2^2- 2^3
        # and so on.
        # Find the righ range.
        # Once the right range is identified, run binary search in it.
        def expoSearch(equation: str) -> int:
            low = 0
            high = 1

            while getEqVal(equation, high) < 0:
                high = high * 2

            # If the loop exits, high will point to end range.
            # We dont need to do complete search from low = 0.
            # low can be end//2
            low = high//2

            while low <= high:
                mid = low + (high-low)//2

                val = getEqVal(equation, mid)

                if val < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return low

        return expoSearch(equation)

obj1 = Solution()
assert obj1.firstPositiveNumber("2*x-20") == 10  # Test Case 1
assert obj1.firstPositiveNumber("2*x-30") == 15  # Test Case 2
assert obj1.firstPositiveNumber("x-45") == 45  # Test Case 3
assert obj1.firstPositiveNumber("5*x-45") == 9  # Test Case 4