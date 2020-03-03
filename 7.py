# what is the 1001st prime #

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# e_sieve finds the greatest prime below a given limit
#  - semi useful, we want something to find the nth prime number
#  - could use sieve, store each found prime in a list, then return the 1001st
#      - this leaves a chance that the 1001st prime is > limit and therefore not in list
def e_sieve(limit):
    primes = {}
    p = 2  # initialize to smallest prime
    aeiou = range(2, limit)  # smallest prime thru limit


