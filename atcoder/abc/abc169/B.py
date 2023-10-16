n = int(input())
al = list(map(int, input().split()))
mul = 1
if 0 in al:
    print(0)
else:
    for a in al:
        mul *= a
        if mul > 10**18:
            print(-1)
            break
    else:
        print(mul)