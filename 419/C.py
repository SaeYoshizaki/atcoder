def main():
    N = int(input())
    Arrx = []
    Arry = []
    for _ in range(N):
        x, y = map(int, input().split())
        Arrx.append(x)
        Arry.append(y)
    Y = max(Arry) - min(Arry)
    X = max(Arrx) - min(Arrx)
    if (Y > X):
        print((Y + 1)//2)
    else:
        print((X + 1)//2)
    
if __name__ == "__main__":
    main()