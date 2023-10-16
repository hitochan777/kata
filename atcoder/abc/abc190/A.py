A, B, C = list(map(int, input().split()))
if A > B:
    print("Takahashi")
elif B > A:
    print("Aoki")
else:
    print("Takahashi" if C == 1 else "Aoki")