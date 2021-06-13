import math
A, B, C = (int(x) for x in input().split())

def solve(A, B, C):
  if C % 2 == 0:
    A = abs(A)
    B = abs(B)

  if A < 0 and B < 0:
    la = math.log(-A) 
    lb = math.log(-B) 
    if la > lb:
      return "<"
    if la == lb:
      return "="

    return ">" 
  if A == 0 and B < 0:
    return ">" 
  if A > 0 and B < 0:
    return ">" 
  if A < 0 and B == 0:
    return "<" 
  if A == 0 and B == 0:
    return "=" 
  if A > 0 and B == 0:
    return ">" 
  if A < 0 and B > 0:
    return "<" 
  if A == 0 and B > 0:
    return "<" 
  if A > 0 and B > 0:
    la = math.log(A) 
    lb = math.log(B) 
    if la > lb:
      return ">"
    if la == lb:
      return "="

    return "<" 

print(solve(A, B, C))