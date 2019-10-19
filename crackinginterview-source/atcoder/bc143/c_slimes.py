n = int(input())
s = input()

cur_slim = s[0]
res = 1

for i in range(1,n):
    if s[i] != cur_slim:
        res += 1
        cur_slim = s[i]

print(res)