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


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def is_prime_two(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        return True
    return False
