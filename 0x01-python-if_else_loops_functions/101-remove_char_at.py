def remove_char_at(str, n):
    j = 1
    if len(str) > n:
        for i in range(len(str) - n):
            str[n] = str[n + j]
