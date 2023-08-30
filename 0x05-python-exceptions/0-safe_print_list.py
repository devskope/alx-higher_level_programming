#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for idx in range(x):
            print(my_list[idx], end="")
            count = count + 1
    except IndexError as e:
        pass
    finally:
        print()
        return count
