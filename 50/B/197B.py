def main():
    H, W, X, Y = map(int, input().split())
    S = []
    ans = 0
    for _ in range(H):
        inputS = list(input())
        S.append(inputS)
    for i in range(1, H):
        if S[X][Y - 1 - i] == "#":
            break
        else:
            ans += 1
    for i in range(1, H):
        if S[X][Y - 1 + i] == "#":
            break
        else:
            ans += 1
    for i in range(1, W):
        if S[X - 1 - i][Y] == "#":
            break
        else:
            ans += 1
    for i in range(1, W):
        if S[X - 1 - i][Y] == "#":
            break
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
