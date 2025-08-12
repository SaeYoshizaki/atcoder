def main():
    N, A, B = map(int, input().split())
    S = list(input())

    for i in range(N-A-B):
        print(S[A+i], end="")

if __name__ == "__main__":
    main()