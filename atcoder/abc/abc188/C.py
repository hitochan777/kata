n = int(input())
rates = list(enumerate((map(int, input().split()))))

for i in range(n-1):
    new_rates = []
    for j in range(len(rates) // 2):
        new_rates.append(rates[j*2] if rates[j*2][1] >  rates[j*2 + 1][1] else rates[j*2+1])

    rates = new_rates


print((rates[0][0] if rates[0][1] < rates[1][1] else rates[1][0]) + 1)