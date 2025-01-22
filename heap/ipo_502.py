import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        cap_to_profit = list(zip(capital, profits))
        heapq.heapify(cap_to_profit)
        heap = []
        while k > 0:
            while cap_to_profit:
                c, p = heapq.heappop(cap_to_profit)
                if w < c:
                    heapq.heappush(cap_to_profit, (c, p))
                    break
                heapq.heappush(heap, -p)
            if heap:
                max_profit_interval = heapq.heappop(heap)
                w += -max_profit_interval
            k -= 1
        return w

        

sol = Solution()
print(sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
print(sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))
print(sol.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]))
print(sol.findMaximizedCapital(1, 2, [1, 2, 3], [1, 1, 2]))
