def solve():
    n = int(input())
    f_t = list(map(lambda x: int(x), input().split()))
    s_t = list(map(lambda x: int(x), input().split()))

    max_team = [0] * (n + 1)
    added_players = []

    for i in range(n):
        if i == 0:
            if f_t[0] > s_t[0]:
                max_team[0] = s_t[0]
                max_team[1] = f_t[0]
                added_players.append('s')
                added_players.append('f')
            else:
                max_team[0] = f_t[0]
                max_team[1] = s_t[0]
                added_players.append('f')
                added_players.append('s')

        else:
            if added_players[i] == 'f':
                f_sum = max_team[i] + s_t[i]
                s_sum = max_team[i-1] + f_t[i]
                if f_sum > s_sum:
                    max_team[i+1] = f_sum
                    added_players.append('l')
                else:
                    max_team[i + 1] = s_sum
                    added_players.append('f')
            else:
                f_sum = max_team[i] + f_t[i]
                s_sum = max_team[i - 1] + s_t[i]
                if f_sum > s_sum:
                    max_team[i + 1] = f_sum
                    added_players.append('f')
                else:
                    max_team[i + 1] = s_sum
                    added_players.append('l')
    print(max_team[n])


solve()

