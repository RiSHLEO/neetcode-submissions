class Solution:
    def isValid(self, s: str) -> bool:
        bracket_list = []
        bracket_dict = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in "{[(":
                bracket_list.append(char)
            if char in bracket_dict:
                if not bracket_list or bracket_list.pop() != bracket_dict[char]:
                    return False
        return not bracket_list