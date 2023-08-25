S = input()
a = S[:len(S)//2]
b = S[len(S)//2+1:]
if a == a[::-1] and b == b[::-1] and S == S[::-1]:
    print("Yes")
else:
    print("No")