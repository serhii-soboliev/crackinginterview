a,b = list(map(lambda x: int(x), input().split()))
r = a - 2*b
print(r if r > 0 else 0)