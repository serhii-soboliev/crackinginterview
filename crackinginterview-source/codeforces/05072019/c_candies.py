n = int(input())
s = input()
li = list(map(int, s.split(" ")))

stc_v = [[0 for i in range(10)] for j in range(10)]
stc_c = [[0 for l in range(10)] for k in range(10)]

for i in range(0, 10):
    for j in range(0, 10):
        stc_v[i][j] = (i + j) % 10
        stc_c[i][j] = 0 if (i + j) < 10 else 1

m  = int(input())

for i in range(m):
    l,r = input().split(" ")
    l = int(l)
    r = int(r)
    print(l)
    print(r)
