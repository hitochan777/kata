import sys

I=sys.stdin.readline

def read_ints():
    return list(map(int, I().split(" ")))

def sum_up_to(num):
    return (num * (num + 1)) // 2

def solve():
    a, b, c, d = read_ints()
    ans = 0
    for z in range(c, d+1):
        p = max(z + 1 - b, b)
        if p > c:
            break

        x_base = z - p + 1
        if x_base < a:
            x_base = a

        y_range = c - p
        x_range = min(x_base - a, y_range)

        l = b - x_base + 1
        r = l + x_range
        ans += sum_up_to(r) - sum_up_to(l-1)
        ans += (b - a + 1) * (y_range - x_range)

    return ans

if __name__ == "__main__":
    print(solve())

        


