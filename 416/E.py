def main():
    inputArr = list(input())
    N = len(inputArr)
    ansArr = ["."] * N

    for i in range(N):
        if inputArr[i] == "#":
            ansArr[i] = "#"
    
    last = -2
    for i in range(N):
        if ansArr[i] == ".":
            if last == -2:
                ansArr[i] = "o"
                last = i
            elif "#" in inputArr[last + 1 : i]:
                ansArr[i] = "o"
                last = i

    print(*ansArr, sep="")

if __name__ == "__main__":
    main()