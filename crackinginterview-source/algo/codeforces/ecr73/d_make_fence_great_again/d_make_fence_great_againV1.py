# https://codeforces.com/problemset/problem/1221/D


def great_fence_cost(n, a, b):
    great_fences = [
        [
            [a[0]], [a[0] + 1], [a[0] + 2]
        ]
    ]
    great_costs = [
        [
            0, b[0], 2*b[0]
        ]
    ]

    for i in range(1, n):
        great_fences.append([])
        great_costs.append([])
        increase_great_fences_and_costs_by_board(great_fences, great_costs, a[i], 0)
        increase_great_fences_and_costs_by_board(great_fences, great_costs, a[i] + 1, b[i])
        increase_great_fences_and_costs_by_board(great_fences, great_costs, a[i] + 2, 2*b[i])

    return min(great_costs[-1][0], great_costs[-1][1], great_costs[-1][2])


def increase_great_fences_and_costs_by_board(great_fences, great_costs, cur_board, cur_cost):

    cur_great_cost = -1
    cur_great_fence = []

    for i in range(3):
        if great_fences[-2][i][-1] != cur_board:
            if cur_great_cost == -1 or cur_great_cost > great_costs[-2][i] + cur_cost:
                cur_great_fence = great_fences[-2][i] + [cur_board]
                cur_great_cost = great_costs[-2][i] + cur_cost

    great_fences[-1].append(cur_great_fence)
    great_costs[-1].append(cur_great_cost)


def solve():
    query_number = int(input())
    for i in range(query_number):
        n = int(input())
        a = []
        b = []
        for j in range(n):
            aj, bj = list(map(int, input().split(" ")))
            a.append(aj)
            b.append(bj)
        print(great_fence_cost(n, a, b))


if __name__ == '__main__':
    solve()

