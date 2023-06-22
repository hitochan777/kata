N = int(input())
def fn(num):
    if num == 0:
        return 1

    return num * fn(num-1)

print(fn(N))
