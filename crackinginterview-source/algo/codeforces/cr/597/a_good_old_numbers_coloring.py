def solve():
    t = int(input())
    for _ in range(t):
        a,b = map(int, input().split())

        a1 = min(a, b)
        b1 = max(a, b)
        a = a1
        b = b1

        if a % 2 == 0 and b % 2 == 0:
            print("Infinite")
        elif a == 1 or b == 2:
            print("Finite")
        elif b % a == 0:
            print("Infinite")
        else:
            s = [0]
            for i in range(10):
                for j in range(10):
                    s.append(i*a + j*b)
            s.sort()

            d = []
            for i in range(1, len(s)):
                d.append(s[i] - s[i-1])

            if d[99] < d[3] or d[99] < d[4] or d[99] < d[5] or d[99] < d[6]:
                print("Finite")
            else:
                print("Infinite")

if __name__ == '__main__':
    solve()
