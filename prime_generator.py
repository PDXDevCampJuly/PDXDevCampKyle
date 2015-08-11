# This file will generate a list of primes
# up to a maximum passed in from the
# command line.
##########################################

from sys import argv

maximum = int(argv[1])
primes = [2, 3, 5]

# A Common Trick:
# notice that an integer n satisfying n % 6 == 2 is divisible by 2,
# as you can write n = 6 * k + 2 for some integer k.
# more generally, after n == 5 we can rule out all integers satisfying
# n % 6 in [0, 2, 3, 4]
# this leaves us integers where n % 6 == 1 or n % 6 == 5 to check.
# the range below gives only integers that satisfy n % 6 == 1
# If this all seems convoluted, you could just check all odds
# for n in range(7, maximum + 1, 2):
for n in range(7, maximum + 1, 6):
    # assume for the moment that n is prime
    is_prime = True
    for p in primes:
        # if n is divisible by some prime in our list,
        if n % p == 0:
            # acknowledge that n is not prime and stop
            is_prime = False
            break
    if is_prime:
        primes.append(n)
    # then test n + 4 as well: (n + 4) % 6 == 5
    # this time I use a list comprehension for demonstration
    if 0 not in [(n + 4) % p for p in primes]:
        primes.append(n + 4)

with open('primes.txt', 'w') as f:
    for p in primes:
        f.write(str(p)+'\n')
    # alternatively
    # f.write('\n'.join([str(p) for p in primes]))
