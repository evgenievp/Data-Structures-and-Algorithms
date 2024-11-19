#https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]


