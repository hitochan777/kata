class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_costs = sorted(costs, key=lambda a: a[1] - a[0])
        total = sum((sorted_costs[i][1] for i in range(len(costs) >> 1)))
        total += sum((sorted_costs[i][0] for i in range(len(costs) >> 1, len(costs))))
        return total
