class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])
                return

            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            next_index = index + 1
            while next_index < len(nums) and nums[index] == nums[next_index]:
                next_index += 1
            backtrack(next_index, path)

        backtrack(0, [])
        return result