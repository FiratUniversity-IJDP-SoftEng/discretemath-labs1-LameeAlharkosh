def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

pseudoprimes = []

for n in range(3, 10001):
    if not is_prime(n):  
        if pow(2, n - 1, n) == 1:
            pseudoprimes.append(n)

print("Pseudoprimes to base 2 (n ≤ 10000):")
print(pseudoprimes)
print("Count:", len(pseudoprimes))

