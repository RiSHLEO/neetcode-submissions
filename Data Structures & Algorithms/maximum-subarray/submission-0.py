class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        largest = -11000
        for i in range(0, len(nums)):
            total += nums[i]

            if total > largest:
                largest = total

            if total < 0:
                total = 0
                
        return largest