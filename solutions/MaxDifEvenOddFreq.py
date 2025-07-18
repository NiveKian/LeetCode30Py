# Maximum Difference Between Even and Odd Frequency

# You are given a string s consisting of lowercase English letters.
# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:
#     a1 has an odd frequency in the string.
#     a2 has an even frequency in the string.
# Return this maximum difference.

# Example 1:
# Input: s = "aaaaabbc"
# Output: 3
# Explanation:
#     The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
#     The maximum difference is 5 - 2 = 3.

class Solution:
    def maxDifference(self, s: str) -> int:
        sDict = {}
        for c in s:
            if c in  sDict:
                sDict[c] += 1
            else:
                sDict[c] = 1
        even_vals = [v for v in sDict.values() if v % 2 == 0]
        odd_vals = [v for v in sDict.values() if v % 2 != 0]
        return (max(odd_vals) - min(even_vals))