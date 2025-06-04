# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:
#     Whitespace: Ignore any leading whitespace (" ").
#     Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
#     Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#     Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

# Return the integer as the final result.

# Example 1:
# Input: s = "42"
# Output: 42
# Explanation:
# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)

class Solution:
    def myAtoi(self, s: str) -> int:
        trim_s = s.lstrip() # remove leading empty spaces
        if not trim_s: return 0

        # check for signed string
        sign = 1
        if not trim_s[0].isdigit():
            if trim_s[0] == "-":
                sign = -1
                trim_s = trim_s[1:]
            elif trim_s[0] == "+":
                trim_s = trim_s[1:]
        
        trim_s = trim_s.lstrip('0') # remove leading zeros
        if not trim_s: return 0

        # Pick up only the numerals, and return on only chars
        num_s = ""
        for c in trim_s:
            if c.isdigit():
                num_s += c
            else:
                break

        if num_s:
            num = sign*int(num_s)
        else:
            return 0

        # If it surpasses the 32-bit treshhold it rounds up the number
        MAX_INT_32 = (2**31 - 1) #2147483647
        MIN_INT_32 = (-2**31) #-2147483648

        if sign < 0:
            result = MIN_INT_32 if num < MIN_INT_32 else num
        else:
            result = MAX_INT_32 if num > MAX_INT_32 else num

        return result