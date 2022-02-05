sx, sy, tx, ty = (int(x) for x in input().split())

W = tx - sx
H = ty - sy

ans = ""
ans += "U" * H + "R" * W
ans += "D" * H + "L" * W
ans += "L" + "U" * (H + 1) + "R" * (W + 1) + "D"
ans += "R" + "D" * (H + 1) + "L" * (W + 1) + "U"
print(ans)