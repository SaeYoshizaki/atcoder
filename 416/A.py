def main():
    N, L, R = map(int, input().split())
    S = list(input())

    for i in range(L-1, R):
        if S[i] == "o":
            continue
        else:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()