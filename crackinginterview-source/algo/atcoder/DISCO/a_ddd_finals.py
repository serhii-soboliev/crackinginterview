x, y = map(int, input().split())

s = 0

if x == 1:
    s += 300000
if y == 1:
    s += 300000

if x == 2:
    s += 200000
if y == 2:
    s += 200000

if x == 3:
    s += 100000
if y == 3:
    s += 100000

if x == 1 and y == 1:
    s += 400000

print(s)
