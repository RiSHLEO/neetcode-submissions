from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def ways(i):
            if i <= 2:
                return i
            return ways(i - 1) + ways(i - 2)

        return ways(n)