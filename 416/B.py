def main():
    inputArr = list(input())
    N = len(inputArr)
    ansArr = ["."] * N

    for i in range(N):
        if inputArr[i] == "#":
            ansArr[i] = "#"
    
    indexArr = [i for i, x in enumerate(ansArr) if x == "#"]
    for i in range(len(indexArr) - 1):
        if indexArr[i] < indexArr[i+1]:
            ansArr[indexArr[i]+1] = "o"
        else:
            pass
    if indexArr[len(indexArr)-1] != len(inputArr):
        ansArr[indexArr[len(indexArr)-1]+1] = "o"
    if indexArr[0] != 0:
        ansArr[0] = "o"
    print(*ansArr, sep="")

if __name__ == "__main__":
    main()