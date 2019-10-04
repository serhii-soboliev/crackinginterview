#https://codeforces.com/contest/1234/problem/C


def is_water_flow_possible(n, row1, row2):
    pass


def solve():
    queries_number = int(input())
    for k in range(queries_number):
        n = int(input())
        row1 = input()
        row2 = input()
        print("YES" if is_water_flow_possible(n, row1, row2) else "NO")


if __name__ == '__main__':
    solve()
