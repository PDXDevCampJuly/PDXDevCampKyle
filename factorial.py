def fact1(n):
    product = 1
    for x in range(1, n+1):
        product *= x
    print("{}! = {}".format(n, product))

def fact2(n):
    if n == 0:
        return 1
    else:
        return fact2(n-1) * n

def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    n = int(input("What number? >> "))
    fact1(n)
    print(fact2(n))
    print("fib({}) = {}".format(n, fib(n)))
