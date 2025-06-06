# failed solution :(

class Solution:
    def findNotStar(self, s: str) -> list:
        indices = []
        for i in range(len(s)):
            if s[i] == '*':
                continue
            if i + 1 < len(s) and s[i + 1] == '*':
                continue
            indices.append(i)
        return indices

    def isMatch(self, s: str, p: str) -> bool:
        pos = 0 # Flag for position in the string
        over = self.findNotStar(p) # check if pattern still has recognitions

        # loops though the pattern
        for i in range(len(p)):
            if p[i] == "*":
                print(f"Reading == {p[i]}")
                print(f"Check Type == Skip")
                continue
            if pos == len(s) and over:
                print(f"Return: False --> Full Pos")
                return False

            # Start the reading of pattern
            print(f"Reading == {p[i]}")
            if  i + 1 < len(p) and p[i+1] == "*":
                # loop "*" check
                print(f"Check Type == * Loop")

                # Define stop
                if over:
                    finder = s.rfind(p[over[0]])
                    stop = finder if finder > 0 else len(s)
                else:
                    stop = len(s)
                print(f" Stop = {stop}")
                
                # Execute the loop
                if p[i] == ".":
                    print(f" Dot Flag == True")
                    while pos < stop:
                        pos += 1
                else:
                    while pos < stop and s[pos] == p[i]:
                        pos += 1
                print(f" Pos = {pos}")
                print(f" str = {s[:pos]}")
            else:
                # Normal Check
                print(f"Check Type == Normal")
                if p[i] != "." and s[pos] != p[i]:
                    print(f"Return: False --> NotMatch")
                    return False
                pos += 1
                print(f" Pos = {pos}")
                print(f" str = {s[:pos]}")

            # remove the already checked ppattern from over
            if over and i == over[0]:
                del over[0]
        
        # Checks if theres string leftovers and returns
        if pos < len(s):
            print(f"Return: False --> Leftovers")
            return False

        print(f"Return: True --> Process Complete")
        return True


            

            
            
