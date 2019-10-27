a = int(input())

b = False
for i in range(1, 10):
    if a % i == 0:
        if a // i < 10:
            b = True
print("Yes" if b else "No")