class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(text):
            stack = []

            for char in text:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        return build(s) == build(t)