def main():
    SArr = []
    CArr = []
    DArr = []
    HArr = []
    N = int(input())
    for _ in range(N):
        pattern, number = map(str, input().split())
        if pattern == "S":
            SArr.append(int(number))
        elif pattern == "C":
            CArr.append(int(number))
        elif pattern == "D":
            DArr.append(int(number))
        else:
            HArr.append(int(number))
    trump = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    difSArr = list(set(trump) ^ set(SArr))
    difCArr = list(set(trump) ^ set(CArr))
    difDArr = list(set(trump) ^ set(SArr))
    difHArr = list(set(trump) ^ set(SArr))

    for i in range(len(difCArr)):
        print('')
if __name__ == "__main__":
    main()