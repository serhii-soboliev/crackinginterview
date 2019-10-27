def fill_with_1(m, x, y):
    m[x][y] = 1
    m[x][y+1] = 1
    m[x+1][y] = 1
    m[x+1][y+1] = 1


def if_2_2_is_1(m, x, y):
    return m[x][y] == 1 and m[x][y+1] == 1 and m[x+1][y] == 1 and m[x+1][y+1] == 1


def solve():
    n, m = list(map(lambda x: int(x), input().split()))
    a = [[0 for x in range(m)] for y in range(n)]
    b = [[0 for x in range(m)] for y in range(n)]
    sol = []

    for i in range(n):
         a[i] = list(map(lambda x: int(x), input().split()))

    for i in range(n-1):
        for j in range(m-1):
            if a[i][j] == 1:
                if if_2_2_is_1(a, i, j):
                    fill_with_1(b, i, j)
                    sol.append([i+1, j+1])
                elif b[i][j] == 0:
                    print(-1)
                    exit()

    print(len(sol))
    for i in range(len(sol)):
        print(sol[i][0], sol[i][1])




solve()
