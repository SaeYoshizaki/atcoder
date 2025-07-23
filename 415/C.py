from math import factorial


def main():
    T = int(input())
    bigArr = [int(input()) for i in range(T*2)]

    for i in range(T):
        kari = bigArr[2*i]
        strkari = list(kari)
    for j in range(len(kari)):
        Arr0 = []
        if kari[j] == "1":
            Arr0.appned(j+1)


def all_positions_from_right(s):
    return [len(s) - i for i, c in enumerate(s) if c == '1']


if __name__ == "__main__":
    main()