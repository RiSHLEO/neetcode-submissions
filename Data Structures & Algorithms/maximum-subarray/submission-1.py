class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        largest = float("-inf")
        for num in nums:
            current += num
            largest = max(largest, current)

            if current < 0:
                current = 0

        return largest