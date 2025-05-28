# First i thought of using deep search through the array
# but than i remembered the concept of maps
# took long than usual sop solve cause i didnt know it required only two numbers (LOL)

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finder = {} # dictionary of values

        # Interates through the list build the dictionary
        for i,n in enumerate(nums):
            complement = target - n
            if complement in finder:
                return [finder[complement], i]
            finder[n] = i  # Store the index of the current number

        return None