def main():
    N = int(input())
    name = [input() for _ in range(N)]
    a, b = a, b = input().split()
    inta = int(a)
    if name[inta - 1] == b:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()