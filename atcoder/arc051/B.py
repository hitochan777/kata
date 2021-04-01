values = [None] * 50
def fib(n: int) -> int:
    if values[n] is not None:
        return values[n]

    if n == 1 or n == 2:
        return 1

    f1 = fib(n-1)
    values[n-1] = f1
    f2 = fib(n-2)
    values[n-2] = f2
    return f1 + f2


K = int(input())
print(fib(K+2), fib(K+1))