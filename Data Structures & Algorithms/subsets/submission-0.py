class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])
                return

            path.append(nums[index])        #include nums[index]
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)     #skip nums[index]

        backtrack(0, [])
        return result