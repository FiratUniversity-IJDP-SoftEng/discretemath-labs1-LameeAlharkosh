import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def random_100_digit_prime():
    while True:
        n = random.randint(10**99, 10**100 - 1)
        if n % 2 == 0:
            n += 1
        if is_prime(n):
            return n

for i in range(1, 11):
    print(f"{i}. {random_100_digit_prime()}\n")
