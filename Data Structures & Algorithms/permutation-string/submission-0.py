class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = {}
        window = {}

        for right in range(len(s1)):
            counts_s1[s1[right]] = counts_s1.get(s1[right], 0) + 1
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            if right >= len(s1):
                window[s2[right - len(s1)]] -= 1
                if window[s2[right - len(s1)]] == 0:
                    del window[s2[right - len(s1)]]
            if counts_s1 == window:
                return True
        return False  