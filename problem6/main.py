def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def full_prima(N):
    prime_digits = {'2', '3', '5', '7'}
    if not is_prime(N):
        return False
    for digit in str(N):
        if digit not in prime_digits:
            return False
    return True

if __name__ == '__main__':
    print(full_prima(2))  # True
    print(full_prima(3))  # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True
