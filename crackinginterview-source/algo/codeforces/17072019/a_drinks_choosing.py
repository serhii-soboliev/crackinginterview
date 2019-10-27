def solve():
    n,k = list(map(lambda x: int(x), input().split()))
    fav_drinks = [0]*k
    for i in range(n):
        d = int(input())
        fav_drinks[d-1] = fav_drinks[d-1] + 1

    odd_count = len([f for f in fav_drinks if f % 2 == 1])
    print(n - odd_count // 2)

solve()