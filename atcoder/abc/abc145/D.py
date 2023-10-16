X, Y = (int(x) for x in input().split())

n = -X + 2 * Y
m = 2 * X - Y

class CombComputer:
    def __init__(self, mod, n):
        self.mod = mod
        self.n = n
        fac = [1, 1]
        ifac = [1, 1]
        inverse = [0, 1]

        for i in range(2, n+1):
            fac.append((fac[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod//i)) % mod)
            ifac.append((ifac[-1] * inverse[-1]) % mod)

        self.fac = fac
        self.ifac = ifac

    def choose(self, k):
        k = min(k, self.n-k)
        return self.fac[self.n] * self.ifac[k] * self.ifac[self.n-k] % self.mod

if n < 0 or m < 0 or (n + m) % 3 != 0:
    print(0)
else:
    n //= 3
    m //= 3
    computer = CombComputer(10**9 + 7, n + m)
    print(computer.choose(n))

