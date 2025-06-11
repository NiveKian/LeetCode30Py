# longest-palindromic-substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Took a long ass time to resolve this one, more than i expected
    # i tried first a more eficient and optimal aproach but my time run out
    # so i solved it the naive way :(
    # will study the Expand Around Center method later

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""  # Dumm var for the string

        # Loops though all characters
        for index in range(len(s)):
            substring = ""

            # Create a crescent substring
            for c in s[index:]:
                substring += c

                # Verify if substring is palindromic
                if substring == substring[::-1]:
                    # Checks for the biggest palindromo
                    if len(substring) > len(longest):
                        longest = substring
        return longest
