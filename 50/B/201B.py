def main():
    moutain = []
    N = int(input())
    for _ in range(N):
        S, T = map(str, input().split())
        T = int(T)
        moutain.append([T, S])
    moutain.sort(reverse=True)
    print(moutain[1][1])


if __name__ == "__main__":
    main()
