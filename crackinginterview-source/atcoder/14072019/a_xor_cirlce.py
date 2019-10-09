def solve():
    n = int(input())
    a = list(map(lambda x: int(x), input().split()))

    res = a[0]
    for i in range(1,n):
        res = res ^ a[i]

    answer = "Yes" if res == 0 else "No"
    print(answer)


solve()