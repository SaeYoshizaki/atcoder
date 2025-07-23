def main():
    TakaArr = list(map(int, input().split()))
    N = TakaArr[0]
    ListenerArr = [list(map(int, input().split())) for _ in range(N)]
    counter = 0

    for i in range(N):
        if TakaArr[1] >= ListenerArr[i][0] and TakaArr[2] <= ListenerArr[i][1]:
            counter += 1
    
    print(counter)


if __name__ == "__main__":
    main()