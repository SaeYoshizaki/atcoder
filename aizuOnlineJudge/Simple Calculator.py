def main():
    while True:
        a, b, c = list(map(str, input().split()))
        a = int(a)
        c = int(c)
        if b == "?":
            break
        if b == "+":
            print(a + c)
        elif b == "-":
            print(a - c)
        elif b == "/":
            print(a // c)
        else:
            print(a * c)


if __name__ == "__main__":
    main()
