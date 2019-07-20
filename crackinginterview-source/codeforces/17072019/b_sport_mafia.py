def maximum_candies_after_n_movies(n):
    return n * (n + 1) // 2


def solve1():
    n,k = list(map(lambda x: int(x), input().split()))
    m = maximum_candies_after_n_movies(n)
    current_candies = n
    eaten_candies = 0
    while m != k:
        m = m - current_candies - 1
        current_candies -= 1
        eaten_candies += 1

    print(eaten_candies)


def solve():
    n, k = list(map(lambda x: int(x), input().split()))
    upper_bound = n
    lower_bound = 0
    while upper_bound > lower_bound:
        if upper_bound == lower_bound + 1:
            u_c = maximum_candies_after_n_movies(upper_bound)
            if u_c == k:
                print(n - upper_bound)
                break

        middle = (upper_bound + lower_bound) // 2
        m_candies = maximum_candies_after_n_movies(middle) - (n - middle)
        if m_candies == k:
            print(n - middle)
            break
        elif m_candies < k:
            lower_bound = middle
        else :
            upper_bound = middle

solve()

