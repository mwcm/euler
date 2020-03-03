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
    # since lcm(a,b,c) ≡ lcm(lcm(a,b),c) we can use reduce to compute the
    # lcm for 20 by walking up the list of integers provided by range until 20
    # eg. lcm(1, 2, 3) == lcm(lcm(1, 2), 3)
    #     lcm(1, 2, 3, 4) == lcm(lcm(lcm(1, 2), 3), 4) etc...

    print(reduce(lcm, range(1, 20 + 1)))

    # equivalent to
    # print(reduce(lcm, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

    # equivalent to
    # lcm(1, 2, 3, 4, 5...... 20) == lcm(lcm(lcm(lcm(lcm(1, 2), 3), 4), 5), ....20)
