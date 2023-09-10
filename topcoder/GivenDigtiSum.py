import math

class GivenDigitSum:
  def construct(self, D, S):
    if D == 1:
      return -1

    n = math.ceil(S / (D-1))
    if n > 9:
      return -1

    li = [S // (D-1)] * (D-1)
    for i in range(S % (D-1)):
      li[i] += 1

    li.sort()
    li.insert(1, 0)
    return int("".join(list(map(lambda c: str(c), li))))

if __name__ == "__main__":
  g = GivenDigitSum()
  print(g.construct(3, 11))