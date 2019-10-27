def calc_prefix_len(precom):
    name = input()
    prefix_len = 0
    used_indexes = [0] * 29
    return str(max(map(lambda c: find_next_index(c, precom, used_indexes), name)) + 1)


def find_next_index(c, precom, used_indexes):
    i = ord(c) - ord('a')
    index = precom[i][used_indexes[i]]
    used_indexes[i] += 1
    return index


def str_to_precom(inp_str, n):
    precom = [[] for i in range(29)]
    [precom[ord(inp_str[i]) - ord('a')].append(i) for i in range(n)]
    return precom


def solve():
    n = int(input())
    precom = str_to_precom(input(), n)
    m = int(input())

    output = "\n".join(map(lambda x: calc_prefix_len(precom), range(m)))
    print(output)


solve()
