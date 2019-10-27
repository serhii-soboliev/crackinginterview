def similar_number(arr):
    m = 1
    for i in range(1, 10):
        i_cnt = arr.count(i)
        m = max(i_cnt, m)
    return m


def subseq_num(arr):
    if len(arr) == 0 or len(arr) == 1:
        return len(arr)

    arr.sort()

    if len(arr) == 2:
        if arr[1] == arr[0] + 1 or arr[1] == arr[0] + 2:
            return 2
        else:
            return 1

    if arr[2] == arr[1] + 1 and arr[1] == arr[0] + 1:
        return 3
    elif arr[2] == arr[1] + 1 or arr[1] == arr[0] + 1 or arr[2] == arr[1] + 2 or arr[1] == arr[0] + 2:
        return 2
    else:
        return 1


def solve():

    cards = input().split()

    s_cards = list(filter(lambda c: c[1] == 's', cards))
    m_cards = list(filter(lambda c: c[1] == 'm', cards))
    p_cards = list(filter(lambda c: c[1] == 'p', cards))

    s_numbers = list(map(lambda c: int(c[0]), s_cards))
    m_numbers = list(map(lambda c: int(c[0]), m_cards))
    p_numbers = list(map(lambda c: int(c[0]), p_cards))

    s_n = similar_number(s_numbers)
    m_n = similar_number(m_numbers)
    p_n = similar_number(p_numbers)

    s_s = subseq_num(s_numbers)
    m_s = subseq_num(m_numbers)
    p_s = subseq_num(p_numbers)

    _n = max(s_n, m_n, p_n, s_s, m_s, p_s)

    print(3 - _n)

solve()