# Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []


from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = { "2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"],
            "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"],
            "8":["t","u","v"], "9":["w","x","y", "z"]}

        out = []

        if digits:
            out = phone.get(digits[0])
        else:
            return out

        for d in digits[1:]:
            dList = phone.get(d)
            out = [d1 + d2 for d1 in out for d2 in dList]

        return out