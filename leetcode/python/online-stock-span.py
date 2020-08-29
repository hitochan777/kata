class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            p, s = self.stack.pop()
            span += s

        self.stack.append((price, span))
        return span


if __name__ == "__main__":
    solver = StockSpanner()
    param_1 = solver.next(price)
    
