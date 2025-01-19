def backspaceCompare(s: str, t: str) -> bool:
    s_right = len(s) - 1
    t_right = len(t) - 1

    s_counter = 0
    t_counter = 0

    while s_right >= 0 and t_right >= 0:
        if s[s_right] != "#" and t[t_right] != "#":
            if s[s_right] != t[t_right]:
                return False
            s_right -= 1
            t_right -= 1

        while (s[s_right] == "#" or s_counter > 0) and s_right >= 0:
            if s[s_right] != "#":
                s_counter -= 1
            else:
                s_counter += 1
            s_right -= 1

        while (t[t_right] == "#" or t_counter > 0) and t_right >= 0:
            if t[t_right] != "#":
                t_counter -= 1
            else:
                t_counter += 1
            t_right -= 1


    return s_right == t_right


print(backspaceCompare("nzp#o#g", "b#nzp#o#g"))
