
# Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Checks if the string can be zigzaged
        if numRows == 1 or numRows >= len(s):
            return s

        numSkip = numRows + (numRows-2)
        holder = []

        # Build the separated strings
        for i in range(numSkip):
            holder.append(s[i::numSkip])

        # Intersect some strings to form zigzag
        for i in range(numRows-2):
            intersec = holder.pop() # remove and return the last string of the holder
            newStr = ''.join(a + b for a, b in zip(holder[i+1], intersec)) # intersect in ZigZag the values
            newStr += holder[i+1][len(intersec):] + intersec[len(holder[i+1]):] # Add the remaining leftovers
            holder[i+1] = newStr

        result = ''.join(holder)
       
        return result
    
        # Analysis
    
        # loop string
        # grab first NRows of chars from the string or string ends
        # pick a NZ(NR<=3 is 1 else NR-2) of chars
        # Repeat

        # P.A.Y.P.A.L.I.S.H.I.R..I..N..G
        # 0.1.2.3.4.5.6.7.8.9.10.11.12.13
        # PAHN [0,4,8,12] = I + (NR+NZ) = 4
        # ALIG [1,5,9,13]
        # YIR  [2,6,10, ]
        # PSI  {3,7,11}   = I + (NR+NZ)

        # Intersections = 3I with 1R; 

        # P.A.Y.P.A.L.I.S.H.I.R..I..N..G
        # 0.1.2.3.4.5.6.7.8.9.10.11.12.13
        # PIN [0,6,12] = I + (NR+NZ) = 6
        # ASG [1,7,13]
        # YH  [2,8]
        # PI  [3,9]
        # AR  {4,10}   = I + (NR+NZ)
        # LI  {5,11}

        # Intersections = 5I with 1R; 
        # Intersections = 4I with 2R; 