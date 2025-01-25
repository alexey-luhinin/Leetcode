class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        is_removed = False

        window_state = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0 and is_removed:
                while nums[left] != 0:
                    window_state -= nums[left]
                    left += 1
                left += 1
                is_removed = False
            if nums[right] == 0 and not is_removed:
                is_removed = True
                continue

            window_state += nums[right]
            result = max(result, window_state)

        return result if is_removed else result - 1

sol = Solution()
print(sol.longestSubarray([1, 1, 0, 1]))
print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(sol.longestSubarray([1,1,1]))
