# spiral matrix

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        newList = []
        flag = "R"

        while any(row for row in matrix):
            match flag:
                case "R":
                    newList.extend(matrix[0])
                    matrix = matrix[1:]
                    flag = "D"
                case "D":
                    for i in range(len(matrix)):
                        newList.append(matrix[i][-1])
                        matrix[i] = matrix[i][:-1]
                    flag = "L"
                case "L":
                    newList.extend(matrix[-1][::-1])
                    matrix = matrix[:-1]
                    flag = "U"
                case "U":
                    for i in range(len(matrix)-1,0,-1):
                        newList.append(matrix[i][0])
                        matrix[i] = matrix[i][1:]
                    flag = "R"

        return newList