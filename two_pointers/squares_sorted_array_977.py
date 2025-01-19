def sorted_squares(nums: list[int]) -> list[int]:
    out = [0] * len(nums)
    left  = 0
    right = len(nums) - 1
    last = len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            out[last] = nums[left]**2
            left+= 1
        else:
            out[last] = nums[right]**2
            right -= 1
        last -= 1

    return out

print(sorted_squares([-4,-1,0,3,10]))

