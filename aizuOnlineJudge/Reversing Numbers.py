def main():
    N = int(input())
    inputArr = list(map(int, input().split()))
    reversedArr = reversed(inputArr)
    print(*reversedArr)

if __name__ == "__main__":
    main()