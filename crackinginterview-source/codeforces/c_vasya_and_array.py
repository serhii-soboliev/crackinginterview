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

    for i in range(len(unsorted_bounds)):
        for j in range(len(sorted_bounds)):
            if is_inside(unsorted_bounds[i], sorted_bounds[i]):
                print("NO")
                quit()

    print('YES')
    r = [0]*n
    for b in unsorted_bounds:
        for i in range(b[0]-1, b[1]):
            r[i] = b[1] + b[0] - i


    a = [0]*n
    for b in sorted_bounds:
        a[b[0]-1:b[1]] = [1]*(b[1] - b[0] + 1)

    c = [0]
    print(",".join(map(str,r)))
    print(",".join(map(str,a)))

def is_inside(f, s):
    return f[0] <= s[0] and s[1] <= f[1]

solve()
