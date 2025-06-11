# median-of-two-sorted-arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged_nums = sorted(nums1 + nums2) # merge and sort the two arrays
        size = len(merged_nums) # size of the new array
        mid_point = size // 2 # mid number point 

        if size % 2 == 0: # if even it calculates
            point = size/2
            return (merged_nums[mid_point-1] + merged_nums[mid_point]) / 2
        else: # if odd it picks the bigger
            return merged_nums[mid_point]