class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current = 1
        longest = 1

        nums.sort()
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i -1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)

        return longest