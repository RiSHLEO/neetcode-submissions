class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        answer = nums[len(nums) - 1]

        while low <= high:
            mid = (low + high) //  2
            if nums[low] <= nums[mid]:                #if left half sorted
                answer = min(answer, nums[low])
                low = mid + 1
            else:                                     #if right half sorted
                answer = min(answer, nums[mid])
                high = mid - 1
        return answer
             