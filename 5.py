# coding: utf-8

from functools import reduce
from math import gcd

# https://stackoverflow.com/questions/19348430/project-euler-getting-smallest-multiple-in-python#19361072

# lcm of a, b is equivalent to: a * b //
# // is divide without remainder
def lcm(a, b):
    """ calculate lowest common multiple of two ints a and b """
    return a * b // gcd(a, b)


# my original solution
# this is very inefficient
def smallest_multiple(max_divisor):
    a_number = max_divisor
    i = 1
    while max_divisor >= i:
        if a_number % i == 0:
            i = i + 1
        else:
            print(f"failed, {a_number} % {i} = {a_number % i}")
            a_number = a_number + 1
            i = 1
    return a_number


if __name__ == "__main__":
    # old fn
    # print(smallest_multiple(20))

    # optimized solution
    # since lcm(a,b,c) ≡ lcm(lcm(a,b),c) we can use reduce to compute the lcm for 20
    # eg. lcm(1, 2, 3) == lcm(lcm(1, 2), 3)
    #     lcm(1, 2, 3, 4) == lcm(lcm(lcm(1, 2), 3), 4) etc...

    print(reduce(lcm, range(1, 20 + 1)))
    # above line is equivalent to
    # print(reduce(lcm, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

    # lcm(1, 2, 3, 4, 5...... 20) is equivalent to: lcm(lcm(lcm(lcm(lcm(1, 2), 3), 4), 5), ....20)

    # reduce looks like this when printing out each iteration:
    # In [10]: reduce(print_and_lcm, aeiou)
    # 1 2             <--- these are the first two items in the list
    # 2 3             <--- 2 is the result of lcm(1, 2), 3 is the next list item
    # 6 4             <--- 6 is lcm(2, 3), 4 is the next list item
    # 12 5            <--- 12 is lcm(6, 4), 5 is the next list item
    # 60 6
    # 60 7
    # 420 8
    # 840 9
    # 2520 10
    # 2520 11
    # 27720 12
    # 27720 13
    # 360360 14
    # 360360 15
    # 360360 16
    # 720720 17
    # 12252240 18
    # 12252240 19     <--- 12252240 is lcm(12252240, 18), 19 is the next list item
    # 232792560 20    <--- 232792560 is lcm(12252240, 19) 20 is next list item
    # Out[10]: 232792560 <--- 232792560 is lcm(232792560, 20) 20 is the last item, so ths is our result
