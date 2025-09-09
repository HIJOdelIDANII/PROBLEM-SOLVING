class Solution:
    def isPalindrome(self, s:str) -> bool:
        newStr = [c.lower() for c in s if c.isalnum()]
        newStr = ''.join(newStr)
        return newStr == newStr[::-1]