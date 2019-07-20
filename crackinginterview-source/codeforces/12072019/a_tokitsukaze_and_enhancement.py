def solve():
    n = int(input())
    m = n % 4
    if m == 1:
        print("0 A")
    elif m == 2:
        print("1 B")
    elif m == 3:
        print("2 A")
    else:
        print("1 A")

solve()