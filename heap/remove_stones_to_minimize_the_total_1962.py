import heapq
import math

class Solution:
    def max_heapify(self, items: list[int]) -> list:
        self.total = 0
        max_heap = []
        for item in items:
            self.total += item
            heapq.heappush(max_heap, -item)

        return max_heap

    def minStoneSum(self, piles: list[int], k: int) -> int:
        max_heap = self.max_heapify(piles)

        for _ in range(k):
            max_item = -heapq.heappop(max_heap)
            flored = math.floor(max_item / 2)
            self.total -= flored
            heapq.heappush(max_heap, -(max_item-flored))

        return self.total

sol = Solution()
print(sol.minStoneSum([5, 4, 9], k=2))
print(sol.minStoneSum([4, 3, 6, 7], k=3))
print(sol.minStoneSum([4, 3, 6, 7], k=30))
