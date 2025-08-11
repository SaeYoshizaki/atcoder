# 10進 → 8進
def to_base_8(x):
    s = ""
    while x > 0:
        s = str(x % 8) + s
        x //= 8
    int_s = int(s)
    return int_s


# 8進 → 10進
def from_base_8(s):
    x = 0
    power = 0
    while s > 0:
        x += (s % 10) * (8**power)
        power += 1
        s //= 10
    return x
