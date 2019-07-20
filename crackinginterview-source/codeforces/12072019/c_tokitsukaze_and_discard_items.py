def search(i,j,_p):
    items_to_remove = []
    for __p in _p:
        if i <= __p <= j:
            items_to_remove.append(__p)
    return items_to_remove


def solve():
    m, n, k = list(map(lambda x: int(x), input().split()))
    p = list(map(lambda x: int(x), input().split()))

    start_search_index = (p[0] // k) * k
    end_search_index = start_search_index + 1
    operations_cnt = 0
    while len(p) > 0:
        items_to_remove = search(start_search_index, end_search_index, p)
        litr = len(items_to_remove)
        if litr > 0:
            operations_cnt += 1
            p = p[litr:]
            start_search_index = items_to_remove[litr - 1] + 1
            end_search_index += litr
        else:
            start_search_index = end_search_index + 1
            end_search_index = start_search_index + k - 1

    print(operations_cnt)



solve()