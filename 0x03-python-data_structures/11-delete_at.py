#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        i = 0
        j = 0
        for itm in my_list:
            if i == idx:
                j += 1
                my_list[i] = my_list[j]
            elif i != (len(my_list) - 1):
                my_list[i] = my_list[j]
            i += 1
            j += 1
        del my_list[-1]
        return my_list
    else:
        return my_list
