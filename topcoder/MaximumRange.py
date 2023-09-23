class MaximumRange:
  def findMax(self, s):
    return max(s.count("+"), s.count("-"))
