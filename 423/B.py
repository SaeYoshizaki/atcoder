def main():
    N = int(input())
    L = list(map(int, input().split()))
    left = 0
    right = N
    for i in range(N):
        if L[i] == 0:
            left = i + 1
        else:
            break
    for j in range(N - 1, -1, -1):
        if L[j] == 0:
            right = j
        else:
            break
    count = max(0, right - left - 1)
    print(count)

if __name__ == "__main__":
    main()