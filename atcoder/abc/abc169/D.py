import math
from collections import defaultdict

cnt = defaultdict(int)
n = int(input())
while n % 2 == 0:
    n //= 2
    cnt[2] += 1

for i in range(3, math.floor(math.sqrt(n)) + 1):
    while n % i == 0:
        cnt[i] += 1
        n //= i

if n > 2:
    cnt[n] += 1

total = sum(math.floor(math.sqrt(2 * c + 1 / 4) - 1 / 2) for c in cnt.values())
print(total)

# k**2 + k < 2 * n 
# k**2 + k - 2 * n < 0
# (k + 1/2) ** 2 - 1 / 4 - 2 * n < 0
# (k + 1/2) ** 2 < 2 * n + 1 / 4
# k + 1/ 2 < sqrt(2 * n + 1 / 4)
# k < sqrt(2 * n + 1 / 4) - 1 / 2