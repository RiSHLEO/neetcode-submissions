class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integers = {}
        result = []
        for num in nums:
            integers[num] = integers.get(num, 0) + 1
        sorted_pairs = sorted(integers.items(), key=lambda pair: pair[1], reverse=True)
        for i in range(k):
            result.append(sorted_pairs[i][0])
        return result