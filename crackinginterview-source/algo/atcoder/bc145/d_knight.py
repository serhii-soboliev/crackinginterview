x, y = map(int, input().split())

n = x + y

if n % 3 != 0:
    print(0)
else:
    n //= 3
    u = x - y if x > y else y - x
    m = (n - u) // 2
    res = 1
    for i in range(n - m + 1, n + 1):
        res *= i
        res %= (10 ** 9 + 7)
    print(res)

# pathes = [[[0, 0]]]
#
# s_pathes = []
#
# new_pathes = []
#
# while pathes:
#     if not pathes:
#         break
#     for path in pathes:
#         last_cell = path[len(path) - 1]
#         new_cells = [[last_cell[0] + 2, last_cell[1] + 1], [last_cell[0] + 1, last_cell[1] + 2]]
#
#         for new_cell in new_cells:
#             if new_cell[0] == x and new_cell[1] == y:
#                 s_pathes.append(path.copy() + [new_cell])
#             elif new_cell[0] < x and new_cell[1] < y:
#                 new_pathes.append(path.copy() + [new_cell])
#
#     pathes = new_pathes
#     new_pathes = []
#
# print(len(s_pathes) % (10 ** 9 + 7))
