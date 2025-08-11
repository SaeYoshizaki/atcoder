def main():
    N, X = map(int, input().split())
    alcohol = 0
    for i in range(N):
        V, P = map(int, input().split())
        alcohol += V * P
        if X * 100 < alcohol:
            print(i + 1)
            exit()
    print(-1)


if __name__ == "__main__":
    main()

# 小数点はなるべく使わない！！
