import math
import random


def element_search(f_list, num):
    print("List : {}".format(f_list))
    print("Number to search: {}".format(num))
    print("Using standard way : {}".format(True if num in f_list else False))

    # binary search
    while True:

        if len(f_list) == 1:
            return True if f_list[0] == num else False
        elif f_list[math.floor(len(f_list) / 2)] == num:
            return True
        elif f_list[math.floor(len(f_list) / 2)] > num:
            f_list = f_list[:math.floor(len(f_list) / 2)]
        else:
            f_list = f_list[math.floor(len(f_list) / 2):]
        continue


print("Using binary search :{}".format(element_search(sorted(random.sample(range(1, 500), 30)), 20)))
