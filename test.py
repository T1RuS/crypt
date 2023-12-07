import random_my


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_coprime(a, b):
    return gcd(a, b) == 1


def get_coprime_num(num):
    while True:
        random_num = random.randint(2, num - 1)
        if is_coprime(num, random_num):
            return random_num


def get_open_key(secret_key, open_global_key):
    return secret_key**2 % open_global_key


p = 5
q = 7
n = p * q
s = get_coprime_num(n)
v = get_open_key(s, n)
r = random.randint(2, n - 1)
x = r**2 % n
print('закрытый ключ', s)
print('открытый ключ', v)
print('x', x, '-> B')
e = random.randint(0, 1)
print(e, '-> A')
y = r*s**e
print('y', y, '-> B')
print(y**2 == x*v**e)
