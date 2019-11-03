def restricted_rps(n, a, b, c, s):
    bob_a = s.count("R")
    bob_b = s.count("P")
    bob_c = s.count("S")

    m_a = min(a, bob_a)
    m_b = min(b, bob_b)
    m_c = min(c, bob_c)
    can_win = m_a + m_b + m_c > n // 2

    how_to_win = ["" for _ in range(n)]

    if can_win:
        u_r = 0 if bob_a >= a else bob_a - a
        u_p = 0 if bob_b >= b else bob_b - b
        u_s = 0 if bob_c >= c else bob_c - c
        u = []
        for i in range(u_r):
            u.append("R")
        for i in range(u_p):
            u.append("P")
        for i in range(u_s):
            u.append("S")

        for i in range(n):
            bob = s[i]
            if bob == "R":
                if b > 0:
                    how_to_win[i] = "P"
                    b -= 1
            if bob == "P":
                if c > 0:
                    how_to_win[i] = "S"
                    c -= 1
            if bob == "S":
                if a > 0:
                    how_to_win[i] = "R"
                    a -= 1

        for i in range(n):
            if how_to_win[i] == "":
                how_to_win[i] = u.pop()

    return can_win, "".join(how_to_win)


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a, b, c = map(int, input().split())
        s = input()

        can_win, how_to_win = restricted_rps(n, a, b, c, s)

        if can_win:
            print("YES")
            print(how_to_win)
        else:
            print("NO")


if __name__ == '__main__':
    solve()
