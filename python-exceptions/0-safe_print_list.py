#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return None
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
