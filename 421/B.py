def main():
    X, Y = map(int, input().split())
    tmp = 0
    for _ in range(8):
        tmp = Y
        Y = reverse(X, Y)
        X = tmp
    print(Y)

def reverse(x, y):
    sum = x + y
    l = [int(x) for x in list(str(sum))]
    l.reverse()
    n = int("".join(map(str,  l)))
    return n
if __name__ == "__main__":
    main()