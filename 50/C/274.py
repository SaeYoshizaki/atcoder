def main():
    N = int(input())
    coordinate = []
    for _ in range(N):
        x, y = map(int, input().split())
        coordinate.append([x, y])
    # judgement
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (coordinate[k][1] - coordinate[i][1]) * (coordinate[j][0] - coordinate[i][0]) == (coordinate[j][1] - coordinate[i][1]) * (coordinate[k][0] - coordinate[i][0]):
                    print("Yes")
                    exit()
    print("No")

if __name__ == "__main__":
    main()


    # (y3 - y1)*(x2 - x1) == (y2 - y1)*(x3 - x1)
    # (coordinate[i+2][1] - coordinate[i][1]) * (coordinate[i+1][0] - coordinate[i][0]) == (coordinate[i+1][1] - coordinate[i][1]) * (coordinate[i+2][0] - coordinate[i][0])