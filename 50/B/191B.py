def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if(X in A):
            A.remove(X) # 多重ループの完成。
        else:
            break
    print(*A)


if __name__ == "__main__":
    main()