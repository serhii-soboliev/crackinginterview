def solve():
    n = int(input())
    s = input()
    li = list(map(int, list(s)))
    if n % 2 == 1 or sum(li) != n/2:
        print(1)
        print(s)
    else:
        print(2)
        print('{} {}'.format(s[0], s[1:]))

solve()