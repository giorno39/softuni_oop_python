import math


def is_prime(num):
    if num <= 1:
        return False
    prime = True
    for n in range(2, num):
        if num % n == 0:
            prime = False
    return prime


def get_primes(seq):
    for num in seq:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))