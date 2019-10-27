n = int(input())
d = list(map(lambda x: int(x), input().split()))

s = 0
for i in range(n):
    for j in range(n):
        if i != j:
            s += d[i]*d[j]

print(s // 2)