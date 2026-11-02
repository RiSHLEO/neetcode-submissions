class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_words = []
        for word in strs:
            encoded_words.append(f"{len(word)}#{word}")
        return "".join(encoded_words)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while(i < len(s)):
            j = s.find("#", i)
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result          
