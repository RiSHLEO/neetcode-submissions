class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        best = high

        while low <= high:
            hours = 0
            mid = (low + high)//2
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        return best