def main():
    H, W = map(int, input().split())
    arr = [list(input().strip()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if arr[i][j] == "#":
                cnt = 0
                if i > 0 and arr[i - 1][j] == "#":
                    cnt += 1
                if j > 0 and arr[i][j - 1] == "#":
                    cnt += 1
                if i < H - 1 and arr[i + 1][j] == "#":
                    cnt += 1
                if j < W - 1 and arr[i][j + 1] == "#":
                    cnt += 1

                if cnt not in (2, 4):
                    print("No")
                    exit()

    print("Yes")


if __name__ == "__main__":
    main()