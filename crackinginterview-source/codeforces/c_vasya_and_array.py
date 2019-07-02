def solve():
    n, m = input().split()
    n = int(n)
    m = int(m)
    sorted_bounds = []
    unsorted_bounds = []
    for i in range(m):
        t, l, r = input().split()
        if int(t) == 1:
            sorted_bounds.append([int(l), int(r)])
        else:
            unsorted_bounds.append([int(l), int(r)])

    r = [0]*(n-1)

    for b in sorted_bounds:
        r[b[0]-1:b[1]-1] = [1]*(b[1] - b[0])

    a = [0]*n
    current = n
    a[0] = current
    for i in range(n - 1):
        if r[i] == 0:
            current -= 1
        a[i + 1] = current

    for b in unsorted_bounds:
        if a[b[0]-1] == a[b[1]-1]:
            print("NO")
            quit()

    print('YES')
    print(" ".join(map(str, a)))

solve()
