# 10進 → N進
def to_base_n(x, N):
    s = ""
    while x > 0:
        s = str(x % N) + s
        x //= N
    int_s = int(s)
    return int_s


# N進 → 10進
def from_base_n(s, N):
    x = 0
    power = 0
    while s > 0:
        x += (s % 10) * (N**power)
        power += 1
        s //= 10
    return x
