def main():
    N, K = map(int, input().split())
    Arr = []
    for _ in range(N):
        A, B = map(int, input().split())
        Arr.append([A, B])
        Arr.sort()
    now_village = 0
    now_village += K
    for i in range(N):
        friend_village = Arr[i][0]
        friend_money = Arr[i][1]
        if now_village >= friend_village:
            now_village += friend_money
        else:
            break
    print(now_village)


if __name__ == "__main__":
    main()
