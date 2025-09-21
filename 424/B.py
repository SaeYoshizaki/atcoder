def main():
    N, M, K = map(int, input().split())
    arr = [[] for _ in range(N)]
    full = set(range(1, M + 1))
    idx = []

    for _ in range(K):
        A, B = map(int, input().split())
        arr[A - 1].append(B)

        if set(arr[A - 1]) == full:
            idx.append(A)
    print(*idx)

if __name__ == "__main__":
    main()