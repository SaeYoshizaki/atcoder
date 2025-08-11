# 10進 → 2進
def to_base_2(x):
    s = ""
    while x > 0:
        s = str(x % 2) + s
        x //= 2
    int_s = int(s)
    return int_s


# 2進 → 10進
def from_base_2(s):
    x = 0
    power = 0
    while s > 0:
        x += (s % 10) * (2**power)
        power += 1
        s //= 10
    return x


def main():
    print(to_base_2(10))


if __name__ == "__main__":
    main()
