def move_zeroes(nums: list[int]) -> None:
    p = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1


nums = [0, 1, 0, 3, 12]
move_zeroes(nums)

print(nums)
