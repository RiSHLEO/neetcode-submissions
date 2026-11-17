class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        best = float("inf")
        left, white_count = 0, 0

        for right in range(len(blocks)):
            if blocks[right] == "W":
                white_count += 1
            if right - left + 1 > k:
                if blocks[left] == "W":
                    white_count -= 1
                left += 1
            if right - left + 1 == k:
                best = min(best, white_count)

        return int(best)