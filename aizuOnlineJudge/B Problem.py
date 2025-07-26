def main():
    a, b = map(int, input().split())
    print(a // b)
    print(a % b)
    result = "{:.5f}".format(a / b)
    print(result)


if __name__ == "__main__":
    main()
