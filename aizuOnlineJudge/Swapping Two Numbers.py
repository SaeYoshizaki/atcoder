import sys


def main():
    inputArr = []
    for line in sys.stdin:
        stripped = line.strip()  # \nを取り除く
        a, b = map(int, stripped.split())
        if a == 0 and b == 0:
            break
        if a > b:
            tmp = a
            a = b
            b = tmp
        inputArr.append([a, b])

    for i in range(len(inputArr)):
        print(*inputArr[i])


if __name__ == "__main__":
    main()


"""
これで良い。
def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
    if (a > b):
        print(b, a)
    else:
        print(b, a)
    


if __name__ == "__main__":
    main()
"""
