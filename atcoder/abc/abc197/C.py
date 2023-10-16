N = int(input())
As = [int(x) for x in input().split()]

minimum = 1 << 31

for partition in range(0, 1 << (N-1)):
    xored = 0
    ored = 0 
    for i in range(N):
        ored |= As[i]
        if partition & 1 == 1:
            xored ^= ored
            ored = 0

        partition >>= 1
    else:
        xored ^= ored

    minimum = min(minimum, xored)

print(minimum)
    