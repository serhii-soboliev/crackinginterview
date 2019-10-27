#https://codeforces.com/contest/1234/problem/C


def is_water_flow_possible(n, top_pipe, bottom_pipe):
    in_flow = [0 for i in range(n)]
    out_flow = [0 for i in range(n)]

    in_flow[0] = 1

    for i in range(n):
        out_flow[i] = 0

        is_dbl_curve = is_double_curve(top_pipe[i], bottom_pipe[i])
        if (is_bottom_inflow(in_flow[i]) and is_dbl_curve) or (is_top_inflow(in_flow[i]) and is_straight(top_pipe[i])):
            out_flow[i] += 1
        if(is_top_inflow(in_flow[i]) and is_dbl_curve) or (is_bottom_inflow(in_flow[i]) and is_straight(bottom_pipe[i])):
            out_flow[i] += 2
        if i < n-1:
            in_flow[i+1] = out_flow[i]

    return is_bottom_inflow(out_flow[n-1])


def is_double_curve(flow1, flow2):
    return is_curve(flow1) and is_curve(flow2)


def is_curve(pipe_num):
    return pipe_num in ['3', '4', '5', '6']


def is_straight(pipe_num):
    return pipe_num in ['1', '2']


def is_top_inflow(flow):
    return flow in [1,3]


def is_bottom_inflow(flow):
    return flow in [2,3]


def solve():
    queries_number = int(input())
    for k in range(queries_number):
        n = int(input())
        row1 = input()
        row2 = input()
        print("YES" if is_water_flow_possible(n, str(row1), str(row2)) else "NO")


if __name__ == '__main__':
    solve()
