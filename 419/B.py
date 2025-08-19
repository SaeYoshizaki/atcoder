def main():
    Q = int(input())
    inputArr = []
    for _ in range(Q):
        first = input().split()
        if first[0] == '1':
            inputArr.append(int(first[1]))
        else:
            print(min(inputArr))
            inputArr.remove(min(inputArr))
if __name__ == "__main__":
    main()