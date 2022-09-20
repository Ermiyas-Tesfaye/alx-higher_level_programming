def uppercase(str):
    i = 0
    value = 0

    for i in range (len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            value = ord(str[i]) - 32
        else:
            value = ord(str[i])
        print(chr(value), end="")
    print("")
