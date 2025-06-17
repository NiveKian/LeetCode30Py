# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
 

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        mini = min(strs, key=len)
        for i in range(len(mini)):
            if all(s and s[i] == mini[i] for s in strs):
                prefix += mini[i]
            else:
                return prefix
        return prefix