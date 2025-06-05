# Palindrome Number
# Given an integer x, return true if x is a, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        og_val = str(x)
        comp_val = []
        mid_val = (len(og_val) - 1) // 2

        for i in range(mid_val + 1):
            comp_val.append(og_val[i])

        if len(og_val) % 2 != 0:
            comp_val.pop()

        for c in og_val[(mid_val+1):]:
            val = comp_val.pop()
            if val != c:
                return False

        return True