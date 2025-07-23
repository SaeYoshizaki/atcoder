def main():
    S = list(input())
    N = len(S)
    printArr = []
    for i in range(N):
        if (S[i] == "#"):
            printArr.append(i+1)
        else:
            pass
    for pair in range(0, len(printArr), 2):
        print(printArr[pair],",",printArr[pair + 1] ,sep='')

if __name__ == "__main__":
    main()