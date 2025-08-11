def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum:int = 0
    for i in range(N):
        sum += A[i]*B[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()