def gcd(a, b):

    while b:
        a %= b
        a, b = b, a
    return a


def is_finite(a, b):
    return gcd(a, b) == 1


def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print("Finite" if is_finite(a,b) else "Infinite")


if __name__ == '__main__':
    solve()
