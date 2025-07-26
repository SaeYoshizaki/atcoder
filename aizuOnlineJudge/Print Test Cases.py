import sys


def main():
    inputArr = []
    for line in sys.stdin:
        stripped = line.strip()  # \nを取り除く
        num = int(stripped)
        if num == 0:
            break
        inputArr.append(num)

    for i in range(len(inputArr)):
        print("Case ", i + 1, ": ", inputArr[i], sep="")


if __name__ == "__main__":
    main()
