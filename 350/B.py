def main():
    N, Q = (int(x) for x in input().split())
    TArr = list(map(int, input().split()))
    print(TArr)
    pullOut = []
    result = N - len(pullOut)
    for i in range(Q):
        if (TArr[i] < N) and TArr[i] not in pullOut:
            pullOut.append(TArr[i])
            print(pullOut)
            print(result)
        else:
            if TArr[i] in pullOut:
                pullOut.remove(TArr[i])
                result += 1
            else:
                result += 1
            print(result)

    print(result)

if __name__ == "__main__":
    main()