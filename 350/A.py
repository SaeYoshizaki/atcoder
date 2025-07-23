def main():
    A = input()
    judgement = 0
    for i in range(1,350):
        a = "ABC" + str(i).zfill(3)
        if A == a and i != 316:
            print("Yes")
            judgement = 1
        else:
            pass
    if judgement == 0:
            print("No")

if __name__ == "__main__":
    main()