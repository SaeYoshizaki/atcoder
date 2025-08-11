def main():
    N, K = map(int, input().split())
    remain = K  # 残金
    count = 0
    Arr = []
    for _ in range(N):
        A, B = map(int, input().split())
        Arr.append([A, B])
        Arr.sort()
    for i in range(N):
        if Arr[i][0] - count <= remain:
            remain = remain - Arr[i][0] + Arr[i][1]
            count += Arr[i][0]
        else:
            print(count + remain)
            exit()
    print(count + remain)


if __name__ == "__main__":
    main()
