def main():
    N, M = map(int, input().split())
    A = list(input())
    B = list(input())
    for b in B:
        if b in A:
            A.remove(b)
    print("".join(A))

if __name__ == "__main__":
    main()