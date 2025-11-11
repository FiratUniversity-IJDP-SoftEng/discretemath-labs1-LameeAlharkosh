def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in range(0, 41):
    value = n**2 + n + 41
    print(f"n = {n}, n^2 + n + 41 = {value}, prime? {is_prime(value)}")

