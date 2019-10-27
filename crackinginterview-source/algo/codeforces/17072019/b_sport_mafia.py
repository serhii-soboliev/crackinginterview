def solve():
    n, k = list(map(lambda x: int(x), input().split()))
    upper_bound = n+1
    lower_bound = -1
    while upper_bound > lower_bound + 1:
        m = (upper_bound + lower_bound) // 2
        if (n - m) * (n - m + 1) // 2 - m > k:
            lower_bound = m
        else:
            upper_bound = m
    print(upper_bound)

solve()

