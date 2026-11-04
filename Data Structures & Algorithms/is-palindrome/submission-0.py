class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_string = "".join(char for char in s if char.isalnum())
        return cleaned_string == cleaned_string[::-1]