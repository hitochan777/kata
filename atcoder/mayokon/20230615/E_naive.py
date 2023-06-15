def count_bitwise_pairs(L):
    count = 0
    for a in range(L + 1):
        for b in range(L + 1):
            if a + b <= L and a ^ b == a + b:
                print(bin(a), bin(b))
                count += 1

    return count % (10**9 + 7)

L = int(input())
result = count_bitwise_pairs(L)
print(result)