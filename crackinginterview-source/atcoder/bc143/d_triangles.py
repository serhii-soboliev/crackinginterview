def find_triangle_count(d):
    n = len(d)
    d.sort()
    res = 0
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n - 1):
            while k < n and d[i] + d[j] > d[k]:
                k += 1
            if k > j:
                res += k - j - 1
    return res


def solve():
    input()
    input_list = list(map(lambda x: int(x), input().split()))
    print(find_triangle_count(input_list))


if __name__ == '__main__':
    solve()