class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        k = len(s1)

        for right, char in enumerate(s2):
            window[char] += 1
            if right >= k:
                window[s2[right - k]] -= 1
            if window == need:
                return True
        return False
