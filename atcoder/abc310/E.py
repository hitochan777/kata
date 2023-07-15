def calculate_sum(S):
    N = len(S)
    cumulative_nand = 1
    total_sum = 0

    for i in range(N):
        if S[i] == '1':
            cumulative_nand = 1 - cumulative_nand

        total_sum += cumulative_nand

    return total_sum

N = int(input())
S = input()
print(calculate_sum(S))