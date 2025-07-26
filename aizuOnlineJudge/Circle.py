import math


def main():
    radius = float(input())
    S = "{:.6f}".format(radius**2 * math.pi)
    length = "{:.6f}".format(2 * radius * math.pi)

    print(S, length)


if __name__ == "__main__":
    main()
