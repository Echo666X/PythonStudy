def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def goldbach_conjecture(N):
    primes = get_primes(N)
    for p in primes:
        q = N - p
        if is_prime(q):
            print(f"{N} = {p} + {q}")
            break

N = int(input())
if N % 2 == 0:
    goldbach_conjecture(N)
else:
    print("Input is not an even number.")
