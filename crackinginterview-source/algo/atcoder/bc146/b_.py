def rotate_string(s, n):
    s = s.lower()
    result = ""
    for i in range(len(s)):
        chr_num = 97 + (((ord(s[i]) + n) - 97) % 26)
        result += chr(chr_num)
    return result.upper()


def solve():
    n = int(input())
    s = input()
    print(rotate_string(s, n))


if __name__ == "__main__":
    solve()
