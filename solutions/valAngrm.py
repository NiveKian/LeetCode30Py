# Valid Anagram

# Given two strings s and t, return true if t is an
# of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicS = {}
        dicT = {}

        for i in range(len(s)):
            dicS[s[i]] = dicS.get(s[i], 0) + 1
            dicT[t[i]] = dicT.get(t[i], 0) + 1

        return dicS == dicT