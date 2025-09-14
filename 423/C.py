def main():
    N, R = map(int, input().split())
    L = list(map(int, input().split()))

    zero = L.count(0)
    if zero == 0:
        print(0)
        return

    left0 = 0
    for i in range(N):
        if L[i] == 0:
            left0 = i
            break
    right0 = 0
    for j in range(N - 1, -1, -1):
        if L[j] == 0:
            right0 = j
            break
    a = left0 + 1
    b = right0 + 1

    count = 0
    if R < a:
        for i in range(R, right0 + 1):
            if L[i] == 1:
                count += 1
    elif R > b:
        for i in range(left0, R):
            if L[i] == 1:
                count += 1
    else:
        for i in range(left0, right0 + 1):
            if L[i] == 1:
                count += 1

    print(zero + 2 * count)

if __name__ == "__main__":
    main()