def totalFruit(fruits: list[int]) -> int:
    window_state = {}
    result = 0
    left = 0

    for right in range(len(fruits)):
        if fruits[right] in window_state:
            window_state[fruits[right]] += 1
        else:
            window_state[fruits[right]] = 1

        while len(window_state) > 2:
            window_state[fruits[left]] -= 1
            if window_state[fruits[left]] == 0:
                del window_state[fruits[left]]
            left += 1

        result = max(result, right - left + 1)
    return result

print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
