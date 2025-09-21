def main():
    a, b, c = map(int, input().split())
    if a == b or b == c or c == a:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()