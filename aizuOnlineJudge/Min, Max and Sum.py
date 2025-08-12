def main():
    n = int(input())
    inputArr = list(map(int, input().split()))
    print(min(inputArr), max(inputArr), sum(inputArr))

if __name__ == "__main__":
    main()