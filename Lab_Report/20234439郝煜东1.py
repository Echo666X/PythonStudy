def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_goldbach_pair(N):
    """Find the smallest prime pair (p, q) such that N = p + q."""
    for p in range(2, N // 2 + 1):
        q = N - p
        if is_prime(p) and is_prime(q):
            print(f"{N} = {p} + {q}")
            break

# Read input
N = int(input())

# Check if the input is within the specified range
if 2 < N <= 2000000000 and N % 2 == 0:
    find_goldbach_pair(N)
else:
    print("Invalid input. Please enter an even number in the range (2, 2 000 000 000].")
