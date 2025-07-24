def main():
    N, Q = (int(x) for x in input().split())
    TArr = list(map(int, input().split()))
    pullOut = []
    for i in range(Q):
        if (TArr[i] < N) and TArr[i] not in pullOut:
            pullOut.append(TArr[i])
        else:
            if TArr[i] in pullOut:
                pullOut.remove(TArr[i])
            else:
                pullOut.append(TArr[i])
    print(N - len(pullOut))


if __name__ == "__main__":
    main()


# 1 7
# 1 1 1 1 1 1 1
