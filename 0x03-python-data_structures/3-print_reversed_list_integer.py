#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    for elm in range(len(my_list)):
        print("{}".format(my_list[::-1][i]))
        i += 1