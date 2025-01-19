def threeSum(nums: list[int]) -> list[list[int]]:
    out = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                out.append((nums[i], nums[left], nums[right]))
                left += 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return out

print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
