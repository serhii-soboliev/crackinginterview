import math
n = int(input())

answer = n - 1

for i in range(int(math.sqrt(n)), 0, -1):
    if n % i == 0:
        answer = n // i + i - 2
        break

print(answer)


