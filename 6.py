# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385

# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025−385=2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sq(n):
    return n ** 2


def sum_squared(limit):
    total = 0
    for num in range(1, limit + 1):
        total += sq(num)
    return total


def square_sum(limit):
    total = sum(range(1, limit + 1)) ** 2
    return total


def difference(limit):
    return square_sum(limit) - sum_squared(limit)


if __name__ == "__main__":
    print(difference(100))
