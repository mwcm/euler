# coding: utf-8


# TODO: try solving with gcd / lcm
# lcm(a,b,c) ≡ lcm(lcm(a,b),c)
# like this: https://stackoverflow.com/questions/19348430/project-euler-getting-smallest-multiple-in-python#19361072


# this is very inefficient
def smallest_multiple(max_divisor):
    a_number = max_divisor
    i = 1
    while max_divisor >= i:
        if a_number % i == 0:
            i = i + 1
        else:
            print(f'failed, {a_number} % {i} = {a_number % i}')
            a_number = a_number + 1
            i = 1
    return a_number

if __name__ is "__main__":
    smallest_multiple(20)
