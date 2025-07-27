def main():
    N, K, Y = map(int, input().split())
    SArr = []
    for i in range(N):
        SArr.append(input())
    SArr.sort()
    Y -= 1
    result = []
    for i in range(K):
        permutation = N ** (K - 1 - i)
        aim = Y // permutation
        result.append(SArr[aim])
        Y %= permutation

    print(''.join(result))

if __name__ == "__main__":
    main()