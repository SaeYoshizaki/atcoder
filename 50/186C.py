def to_base_N(x, N):
    s = ""
    while x > 0:
        s = str(x % N) + s
        x //= N
    int_s = int(s)
    return int_s


def judge_10(N):
    N = str(N)
    if "7" in N:
        return True
    else:
        return False


def judge_8(base8):
    base8 = str(base8)
    if "7" in base8:
        return True
    else:
        return False


def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if judge_10(i) == False and judge_8(to_base_N(i, 8)) == False:
            count += 1
            # print(i)
    print(count)


if __name__ == "__main__":
    main()
