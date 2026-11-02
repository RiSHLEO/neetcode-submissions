class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for item in s:
            s_dict[item] = s_dict.get(item, 0) + 1
        for item in t:
            t_dict[item] = t_dict.get(item, 0) + 1
        if s_dict == t_dict:
            return True
        return False

