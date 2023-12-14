import random_my

PRIMES = [3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 43]


def find_mod_inv(num, mod):
    """ Нахождение обратного числа """
    for x_l in range(1, mod):
        if (num % mod) * (x_l % mod) % mod == 1:
            return x_l


def get_quadratic_deduction(num, mod):
    """ Нахождение минимального квадратичного вычета """
    quadratic_deduction_count = 1
    while quadratic_deduction_count < mod:
        if quadratic_deduction_count**2 % mod == num % mod:
            return quadratic_deduction_count

        quadratic_deduction_count += 1

    return None


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_coprime(a, b):
    return gcd(a, b) == 1


def multiplication_numbers(keys_list, e_list):
    result = 1
    for i in range(len(keys_list)):
        result *= keys_list[i]**e_list[i]

    return result


def bin_power(a, b, n):
    if b == 0:
        return 1
    if b % 2 == 0:
        return bin_power(a * a % n, b // 2, n)
    else:
        return a * bin_power(a * a % n, b // 2, n) % n


def is_prime(a, count_iter=5):
    if a < 4:
        return a == 2 or a == 3
    for i in range(count_iter):
        if bin_power(PRIMES[i], a - 1, a) != 1:
            return False
    return True


def is_prime_two(a, k=5):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    r, s = 0, a - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        p = 0
        while p < 2:
            p = random_my.random(a - 1)
        x = pow(p, s, a)
        if x == 1 or x == a - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, a)
            if x == a - 1:
                break
        else:
            return False
    return True
