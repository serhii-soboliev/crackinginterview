import math

from utils.constants import SPACE, LINE_WRAP


def justify_text(words, max_line_symbols):
    n = len(words)
    words_len = list(map(lambda x: len(x), words))
    if sum(words_len) <= max_line_symbols:
        justified_text = " ".join(words)
        return justified_text

    lc = build_lines_cost_matrix(words, max_line_symbols)

    min_cost = [0 for _ in range(n)]
    result = [0 for _ in range(n)]
    for i in reversed(range(n)):
        min_cost[i] = lc[i][n-1]
        result[i] = n
        for j in range(n-1, i, -1):
            if math.isinf(lc[i][j - 1]):
                continue
            elif min_cost[i] > min_cost[j] + lc[i][j-1]:
                min_cost[i] = min_cost[j] + lc[i][j - 1]
                result[i] = j

    res = ""
    i = 0
    while True:
        j = result[i]
        for k in range(i, j-1):
            res += words[k] + SPACE
        res += words[j-1]
        i = j
        if j >= n:
            break
        res += LINE_WRAP
    return res


def cost_function(spaces_num):
    return spaces_num ** 2


def calc_cost_of_text_justification(words, max_line_symbols):
    n = len(words)
    lc = build_lines_cost_matrix(words, max_line_symbols)

    min_cost = [0 for _ in range(n)]
    result = [0 for _ in range(n)]
    for i in reversed(range(n)):
        min_cost[i] = lc[i][n - 1]
        result[i] = n
        for j in range(n-1, i, -1):
            if math.isinf(lc[i][j - 1]):
                continue
            elif min_cost[i] > min_cost[j] + lc[i][j - 1]:
                min_cost[i] = min_cost[j] + lc[i][j - 1]
                result[i] = j

    return min_cost[0]


def build_lines_cost_matrix(words, max_line_symbols):
    n = len(words)
    words_len = list(map(lambda x: len(x), words))
    lines_cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        lines_cost[i][i] = cost_function(max_line_symbols - words_len[i])
        for j in range(i + 1, n):
            t_cost = sum(words_len[i:j + 1]) + j - i
            lines_cost[i][j] = cost_function(max_line_symbols - t_cost if t_cost <= max_line_symbols else math.inf)
    return lines_cost

