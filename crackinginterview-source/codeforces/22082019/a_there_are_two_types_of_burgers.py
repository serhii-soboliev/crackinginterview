def solve():
    n = int(input())
    burgers = []
    prices = []
    for i in range(n):
        burgers.append(input())
        prices.append(input())

    for i in range(n):
        b, p, f = list(map(lambda x: int(x), burgers[i].split()))
        h, c = list(map(lambda x: int(x), prices[i].split()))

        max_burgers = b // 2
        max_price = h if h > c else c
        min_price = c if c <= h else h
        first_burger = p if max_price == h else f
        second_burger = f if first_burger == p else p

        f_cost = max_price * min(max_burgers, first_burger)
        burgers_left = (max_burgers - first_burger) if max_burgers > first_burger else 0
        print("")
        print(f_cost + min_price*min(burgers_left, second_burger), end=" ")


solve()

