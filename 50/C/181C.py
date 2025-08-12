def main():
    N = int(input())
    Arr =[]
    for _ in range(N):
        x, y = map(int, input().split())
        Arr.append([x, y])
    for i in range(N-2):
        y1 = Arr[i+2][1]-Arr[i][1]
        y2 = Arr[i+1][1]-Arr[i][1]
        x1 = Arr[i+1][0]-Arr[i][0]
        x2 = Arr[i+2][0]-Arr[i][0]
        if y1 * x1 == y2 * x2:
            print("Yes")
            exit()
    print("No")
if __name__ == "__main__":
    main()