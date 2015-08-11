# this script should take an integer up to 10000 as input and print
# the prime factorization of it as follows:
# 60 = 2^2 * 3 * 5
# Feel free to use the list of primes in primes.txt
from sys import argv
from collections import Counter

target = int(argv[1])
with open("primes.txt") as f:
    primes = f.read().split('\n')[:-1] # ignore the last empty line of the file

# convert primes from strings to integers
primes = [int(p) for p in primes]

# or without list comprehension
# list = []
# for p in primes:
#     list.append(int(p))
# primes = list

factorList = []
remainder = target
for p in primes:
    while remainder % p == 0:
        factorList.append(p)
        remainder = remainder / p
    if remainder == 1:
        break

# print "prime factors of %d are: " % target
strs = []
for factor in factorList:
    strs.append(str(factor))
# strs = [str(factor) for factor in factorList]
print("{} =".format(target), " * ".join(strs))

# format somewhat more nicely with Counters
factors = Counter(factorList)
output = ["{}^{}".format(x, factors[x]) if factors[x] > 1 else str(x) for x in sorted(list(factors.keys()))]
print('{} ='.format(target), ' * '.join(output))
