def findZeroOne(X):
  
  best = 0
  temp = 0
  
  for i,n in enumerate(X):
    # Build the verificaition variables
    last = None if i == 0 else X[i-1]
    next = None if i == len(X)-1 else X[i+1]
    valid = True if (n != last) and (n != next) else False
    
    # validate the variables
    if valid:
      temp += 1
    else:
      if temp > best: best = temp
      temp = 0
      
  if temp > best: best = temp
  
  return best
  
  
print(f"Test: 1 Result: {findZeroOne([0])} Expected: 1")
print(f"Test: 2 Result: {findZeroOne([0,1])} Expected: 1")
print(f"Test: 3 Result: {findZeroOne([0,1,0])} Expected: 3")
print(f"Test: 4 Result: {findZeroOne([1,0,1])} Expected: 3")
print(f"Test: 5 Result: {findZeroOne([1,1,0,1])} Expected: 2")
print(f"Test: 6 Result: {findZeroOne([1,0,0,1])} Expected: 1")
print(f"Test: 7 Result: {findZeroOne([0,1,0,1,0])} Expected: 5")