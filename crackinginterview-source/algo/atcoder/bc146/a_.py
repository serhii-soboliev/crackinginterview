def solve():
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    day = input()
    idx = days.index(day)
    print(7 - idx)


if __name__ == "__main__":
    solve()
