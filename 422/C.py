def main():
    T = int(input())
    for _ in range(T):
        A, B, C = map(int, input().split())
        print(min(A, C, (A+B+C)//3))

if __name__ == "__main__":
    main()