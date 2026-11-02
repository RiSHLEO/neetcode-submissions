class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            required_num = target - num
            if required_num in num_dict:
                return [num_dict[required_num], index] 
            num_dict[num] = index