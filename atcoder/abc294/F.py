N, M, K = map(int, input().split())

# 高橋君の砂糖水を砂糖の割合でソート
sugars_t = []
for i in range(N):
    a, b = map(int, input().split())
    sugar_ratio = a / b
    sugars_t.append(sugar_ratio)
sugars_t.sort()

# 青木君の砂糖水を砂糖の割合でソート
sugars_a = []
for i in range(M):
    c, d = map(int, input().split())
    sugar_ratio = c / d
    sugars_a.append(sugar_ratio)
sugars_a.sort()

# 砂糖水を混ぜた時の割合を計算し、降順にソート
mixtures = []
for i in range(N):
    for j in range(M):
        sugar_ratio = (sugars_t[i] + sugars_a[j]) / (1 + sugars_t[i] * sugars_a[j])
        mixtures.append(sugar_ratio)
mixtures.sort(reverse=True)

# 濃度が高い方からK番目までの割合を取り出す
top_k = mixtures[:K]

# 濃度が高い方からK番目の砂糖水の濃度を計算する
max_ratio = max(top_k)
result = 100 * max_ratio / (1 + max_ratio)

print(result)
