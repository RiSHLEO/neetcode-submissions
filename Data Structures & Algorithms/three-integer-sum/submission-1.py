class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                total = nums[left] + nums[right]
                if total == -nums[i]:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > -nums[i]:
                    right -= 1
                else:
                    left += 1
        return [list(t) for t in result]