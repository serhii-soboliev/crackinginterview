def trivial_platform(n, m, c):
    res = [0] * n
    cur_pos = 0
    for i in range(m):
        for j in range(cur_pos, cur_pos + c[i]):
            res[i] = j+1
            cur_pos += 1
    return True, res


# todo fix
def jump_program(n, m, d, c):
    res = [0]*n
    if n < d:
        return trivial_platform(n, m, c)

    cur_pos = -1
    for i in range(0, m):
        start_pos = cur_pos + d
        pl = c[i]
        for j in range(start_pos, start_pos+pl):
            if j < n:
                res[j] = i+1
        cur_pos = start_pos + pl - 1

    zero_len = 0
    for i in range(n-1, 0, -1):
        if res[i] == 0:
            zero_len += 1
        else:
            break

    return zero_len < d, res


def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    can, res = jump_program(n, m, d, c)
    if can:
        print("YES")
        print(' '.join(map(str, res)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()
