class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        length = len(nums)
        window_state = 0

        left = 0

        for i in range(len(nums)):
            window_state += nums[i]
            while window_state - nums[left] >= target:
                window_state -= nums[left]
                left += 1

            if window_state >= target:
                length = min(length, i - left + 1)

        return length if window_state >= target else 0

sol = Solution()

print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
print(sol.minSubArrayLen(4, [1, 4, 4]))
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
