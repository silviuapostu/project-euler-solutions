# coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)
# How many different ways can £2 be made using any number of coins?

from itertools import product

coin_values = {1, 2, 5, 10, 20, 50, 100, 200}


def factor_combs(total, factors, n_combs=0):
    max_f = max(factors)
    if len(factors) == 0:
        return "Please provide a list of factors!"
    if len(factors) == 1:
        return n_combs+1 if total % max_f == 0 else n_combs
    else:
        for mul in range(total//max_f+1):
            factors_cp = factors[:]
            factors_cp.remove(max_f)
            n_combs = factor_combs(total-mul*max_f, factors_cp, n_combs)
    return n_combs


def coin_sums(total_pence=200):
    global coin_values
    coin_values = sorted(list(coin_values), reverse=True)
    return factor_combs(total_pence, coin_values)


def coin_sums_brutef(total_pence=200):
    global coin_values
    val_mult = []

    for v in coin_values:
        vm = [
            i * v for i in range(total_pence // v + 1)
            if i * v % 2 == 0 or i * v % 5 == 0]
        val_mult.append(vm)

    valid_combos = [c for c in product(*val_mult) if sum(c) == total_pence]
    return len(valid_combos)


if __name__ == '__main__':
    # print(coin_sums_brutef())
    print(coin_sums())
