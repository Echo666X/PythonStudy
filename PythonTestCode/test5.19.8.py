

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def generate_palindrome_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_palindrome(num):
            print("{:6}".format(num), end=" ")
            count += 1
            if count % 10 == 0:
                print()
        num += 1

n = int(input())
generate_palindrome_primes(n)