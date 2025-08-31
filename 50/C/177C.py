def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    result = 0
    mod = 10**9 + 7
    for i in range(N-1):
        A_sum -= A[i]
        result += A[i] * A_sum
    ans = int(result) % mod
    print(ans)


if __name__ == "__main__":
    main()