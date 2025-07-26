def main():
    height, width = map(int, input().split())
    S = height * width
    length = (height + width) * 2
    print(S, length)


if __name__ == "__main__":
    main()
