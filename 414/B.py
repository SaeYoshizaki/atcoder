def main():
    N = int(input())
    InputArr = [input().split() for _ in range(N)]

    charArr = []
    intArr = []

    for i in range(N):
        charArr.append(InputArr[i][0])

    for j in range(N):
        intArr.append(int(InputArr[j][1]))

    if sum(intArr) > 100:
        print("Too Long")

    else:
        for k in range(N):
            for l in range(intArr[k]):
                print(charArr[k], end="")


if __name__ == "__main__":
    main()
