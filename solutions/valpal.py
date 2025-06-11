# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

 
# Example 1:
# Input: s = "()"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        d = {"[": "]", "{": "}", "(": ")"}
        flag = []

        for c in s:
            if c in d:
                flag.append(d[c])
            elif c in d.values():
                if flag:
                    p = flag.pop()
                    if p != c: return False
                else:
                    return False
                
        return len(flag) == 0