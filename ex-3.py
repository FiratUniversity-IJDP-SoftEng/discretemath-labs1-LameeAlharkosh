def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for p in range(2, 101):
    if is_prime(p):
        mersenne = 2**p - 1
        if is_prime(mersenne):
            print(f"2^{p} - 1 = {mersenne} is prime")
        else:
            print(f"2^{p} - 1 = {mersenne} is not prime")

