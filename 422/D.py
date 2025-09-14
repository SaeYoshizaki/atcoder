def main():
    N, K = map(int, input().split())
    a = [K]
    for _ in range(N):
        new_a = []
        for x in a:
            left = x // 2
            right = x - left
            new_a.extend([left, right])
        a = new_a
    if K % (2**N) == 0:
        X = 0
    else:
        X = 1
    print(X)
    print(*a)

if __name__ == "__main__":
    main()