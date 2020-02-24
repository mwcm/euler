# coding: utf-8
import math

# largest prime factor of 600851475143

# your first solution (almost working?) extremely slow
"""
# solution = 486847
curr = 0
for i in range(2, int(sqrt(600851475143))):
    if (600851475143 % i) != 0:
        pass
    else:
        for j in range(2, int(sqrt(i))):
            if (i % j) != 0:
                pass
            else:
                curr = i
                print(curr)


# skip evens solution
def primeFactors(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i and divide n
        while n % i == 0:
            print(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


# another working solution
# def biggest_prime_multiple(number):

    i_prime = number
    biggest_prime = 1

    for i in range(2, number):
        while i_prime % i == 0:
            i_prime = i_prime // i
            biggest_prime = i
        if 1 == i_prime:
            break

    return biggest_prime



# this finds factors of 600851475143
# for i in range(2, 600851475143):
    # if 600851475143 % i == 0:
        # print(i)
"""

# key insight here is that every whole number breaks into primes,
# we can use the idea of a Factor Tree to break down the number into it's factors
def largest_prime_factor(n):
    biggest = 1
    curr = n
    for i in range(2, n):  # for each i between 2 and n
        while curr % i == 0:  # if 0 this is a prime factor
            curr = curr // i
            # find the next biggest up the tree by floor division
            # of the original number by the current factor
            biggest = i  # update current biggest prime with result
        if 1 == curr:
            break  # break out if we get down to 1, no more factors remain
    return biggest


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
