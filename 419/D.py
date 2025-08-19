def main():
    N, M = map(int, input().split())
    S = list(input())
    T = list(input())
    for _ in range(M):
        Skari = []
        Tkari = []
        X, Y = map(int, input().split())
        Skari = S[X-1:Y]
        Tkari = T[X-1:Y]
        S[X-1:Y] = Tkari
        T[X-1:Y] = Skari
    print(*S, sep='')

if __name__ == "__main__":
    main()