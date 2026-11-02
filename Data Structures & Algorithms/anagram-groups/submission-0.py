class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for word in strs:
            label = "".join(sorted(word))
            sorted_dict.setdefault(label, []).append(word)
        return list(sorted_dict.values())

        