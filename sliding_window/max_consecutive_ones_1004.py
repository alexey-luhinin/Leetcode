def longestOnes(nums: list[int], k: int) -> int:
    window_state = 0
    result = 0
    counter = 0

    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            counter += 1

        while counter > k:
            if nums[left] == 0:
                counter -= 1
            window_state -= 1
            left += 1

        window_state += 1
        result = max(result, window_state)

    return result

print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
