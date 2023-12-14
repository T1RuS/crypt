from _decimal import Decimal


def gen_random(seed, seed2, i):
    state1 = seed
    state2 = seed2
    state3 = seed + seed2
    state4 = state3 * i
    state5 = 3434.2
    s = id(state1) * id(state2) + id(state3) / id(state4) * id(state5)
    s = hash(s)
    del state1
    return s


def random(bound):
    mi = float('+inf')
    t = None
    ma = 0
    seed = 24
    seed2 = 43
    iterations = 1000
    randoms = set()
    for i in range(iterations):
        r = gen_random(seed, seed2, i)
        randoms.add(r)
        mi = min(mi, r)
        ma = max(ma, r)
        seed = r
        y = r/(i + 1) * seed2
        seed2 = id(y)
        if i == (iterations // 2):
            t = r

    reversed_l = [int(str(p)[::-1]) for p in randoms]
    ordered = sorted(list(reversed_l))
    pos = ordered.index(int(str(t)[::-1]))

    rand_num = int(pos/len(randoms) * bound)
    if rand_num:
        return int(pos/len(randoms) * bound)
    return random(bound)
