class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = []
        product = 1

        for num in nums:
            left.append(product)
            product *= num

        right = [1] * n
        product = 1

        for i in reversed(range(n)):
            right[i] = product
            product *= nums[i]

        return [l * r for l, r in zip(left, right)]