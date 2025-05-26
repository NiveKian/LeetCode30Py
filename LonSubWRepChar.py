# 3: longest-substring-without-repeating-characters

# Given a string s, find the length of the longest

# without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = list(s)
        substring = ""
        best = 0

        for c in chars:
            if c not in substring:
                substring += c
            else:
                index = substring.find(c)
                substring = substring[index+1:] + c
            best = max(best, len(substring))
        
        return best