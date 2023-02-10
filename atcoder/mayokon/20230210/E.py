N = int(input())
A = [int(x) for x in input().split()]

MOD = 10**9 + 7
MAX = 10**6+10
prime = [0 for i in range(MAX)]
max_map = dict()


def sieve():
    prime[0], prime[1] = 1, 1
    for i in range(2, MAX):
        if prime[i] == 0:
            for j in range(i * 2, MAX, i):
                if prime[j] == 0:
                    prime[j] = i
            prime[i] = i


def lcmModuloM(arr, mod):
    for i in range(len(arr)):
        num = arr[i]
        temp = dict()
        while num > 1:
            factor = prime[num]
            if factor in temp.keys():
                temp[factor] += 1
            else:
                temp[factor] = 1
            num = num // factor

        for i in temp:
            if i in max_map.keys():
                max_map[i] = max(max_map[i], temp[i])
            else:
                max_map[i] = temp[i]

    ans = 1
    for i in max_map:
        ans = (ans * pow(i, max_map[i], mod)) % mod
    return ans


sieve()
lc = lcmModuloM(A, MOD)
ans = 0
for a in A:
    ans += lc * pow(a, MOD-2, MOD)
    ans %= MOD

print(ans)
