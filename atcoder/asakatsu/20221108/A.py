A = list(chr(ord('a') + int(x) - 1) for x in input().split())
print("".join(A))