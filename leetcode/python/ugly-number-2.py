class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        p2, p3, p5 = 0, 0, 0
        while len(uglies) < n:
            two = uglies[p2] * 2
            three = uglies[p3] * 3
            five = uglies[p5] * 5
            next_ugly = min(two, three, five)
            if next_ugly == two:
                p2 += 1
            elif next_ugly == three:
                p3 += 1
            else:
                p5 += 1
            
            if uglies[-1] < next_ugly:
                uglies.append(next_ugly)
            
        return uglies[-1]
