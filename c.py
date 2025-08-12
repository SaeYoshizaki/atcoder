def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    dict = {}

    newArr = [A[i] + i for i in range(N)]
    for j in range(N):
        dict_key = j - A[j]
        if dict_key not in dict:
            dict[dict_key] = 0
        dict[dict_key] += 1
    for k in newArr:
        if k in dict:
            count += dict[k]
    print(count)

if __name__ == "__main__":
    main()