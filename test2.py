from mathematical_operations import find_mod_inv, get_quadratic_deduction, is_coprime, multiplication_numbers
from random_my import random


p = 5
q = 7
n = p * q


def get_keys(mod, quantity_num):
    private_keys = []
    public_keys = []

    for i in range(quantity_num):
        while True:
            random_num = random(mod - 1)
            mod_inv = find_mod_inv(random_num, mod)
            if mod_inv:
                quadratic_deduction_num = get_quadratic_deduction(mod_inv, mod)
                if random_num not in public_keys and quadratic_deduction_num is not None and is_coprime(random_num, mod):
                    public_keys.append(random_num)
                    private_keys.append(quadratic_deduction_num)
                    break

    return public_keys, private_keys


k = 4

v, s = get_keys(n, k)

print(v, s)


probability_list = [random(2) for i in range(k)]

r_list = [34, 12, 56, 67, 87, 34, 87, 89, 45]
for r in r_list:
    x = (r**2) % n
    y = (r * multiplication_numbers(s, probability_list)) % n
    print((y**2 * multiplication_numbers(v, probability_list)) % n == x)
