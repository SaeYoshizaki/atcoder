import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)
# gcdで最大公約数を求めることができる。
# xとyの積をそれで割っている。

def main():
    A, B = map(int, input().split())
    print(lcm(A, B))

if __name__ == "__main__":
    main()