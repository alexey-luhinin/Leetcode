class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_state = 0
        result = float("-inf")

        left = 0

        for i in range(len(nums)):
            window_state += nums[i]
            if i - left + 1 == k:
                result = max(result, window_state)
                window_state -= nums[left]
                left += 1

        return result / k

sol = Solution()

print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
print(sol.findMaxAverage([5], 1))
