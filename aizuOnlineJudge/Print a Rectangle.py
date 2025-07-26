def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        for _ in range(a):
            print("#"*b)
        print()

if __name__ == "__main__":
    main()