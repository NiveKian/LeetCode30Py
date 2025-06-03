# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Observations:
# I studied a bit latter after resolving and theres a arithimetical way to resolve this problem
# maybe i will try aproching problems this way next time for better performance

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT_32 = (2**31 - 1)
        sig = 1 if x >= 0 else -1
        result = int(str(abs(x))[::-1])

        if abs(result) > MAX_INT_32:
            return 0
        
        return result*sig
